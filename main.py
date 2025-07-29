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
    print(user_input)
    gpt_response=text_to_data(user_input)

    #gpt_response to DF

    extracted_data= gpt_to_df(gpt_response)
    print(extracted_data)

    table_html = extracted_data.to_html(classes='table table-bordered', index=False)
    pie_chart_html=df_to_pie(extracted_data)


    return render_template_string(html, submitted=submitted, user_input=user_input,
                              table_html=table_html, pie_chart_html=pie_chart_html)
    # sending test to llm for insights
    

if __name__ == "__main__":
    app.run(debug=True)