from flask import Flask, request, render_template_string
from web_page import *
from helper import * 
import pandas as pd


app = Flask(__name__)

# HTML template with a simple input form


@app.route("/", methods=["GET", "POST"])
def input_page():
    submitted = False
    user_input = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        submitted = True
    # print(user_input)
    gpt_response=text_to_data(user_input)

    #gpt_response to DF
    json_res=gpt_to_data(gpt_response)
    table_html = data_to_html_table(json_res)

    pie_chart_html=data_to_pie_chart(json_res)


    return render_template_string(html, submitted=submitted, user_input=user_input,
                              table_html=table_html, pie_chart_html=pie_chart_html)
    # sending test to llm for insights
    

if __name__ == "__main__":
    app.run(debug=True)
