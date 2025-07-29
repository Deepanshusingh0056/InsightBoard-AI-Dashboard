import requests
import json
import pandas as pd 
import matplotlib.pyplot as plt
import io
import base64

# Replace with your actual API key and site details
def text_to_data(transcript):

    prompt = f"""From the transcript below, extract all key tracks discussed during the meeting. For each track, return:
    - title of the track
    - current status (e.g., completed, in progress, pending)
    - priority level (e.g., P0, P1, P2)

    Respond in JSON list format like:
    [
    {{
        "title": "<Track Title>",
        "status": "<Status>",
        "priority": "<Priority>"
    }},
    ...
    ]

    Note : 
    1.please return the result in array of json 
    2. Please return Status only from ['Completed','In Progress', 'Yet To Start']
    3. Return Priority only from [P0,P1,P2]


    Transcript:
    {transcript}

    
    """

    # API request payload

    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": "AIzaSyCg2zOKnPjCZerKaQThN-rnMJ6DprXMCro"
    }

    # The content you'd like summarized

    # Prompt to Gemini model
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    return response 

def gpt_to_df(response):
    
    try :
        output =response.json()
        res=output['candidates'][0]['content']['parts'][0]['text']
        res=res.replace('json','').replace('\n','').replace('`','')
        data = json.loads(res)
        df=pd.DataFrame(data)

        return df
    except Exception as e :
        print(e)
    return pd.DataFrame(columns=['title','status','priority'])



def df_to_pie(df):
    status_counts = df['status'].value_counts()
    print(status_counts)
    # Generate pie chart
    fig, ax = plt.subplots()
    ax.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=140)
    ax.set_title("Task Status Distribution")

    # Save figure to a byte stream and encode as base64
    img_stream = io.BytesIO()
    plt.savefig(img_stream, format='png')
    img_stream.seek(0)
    pie_chart_base64 = base64.b64encode(img_stream.getvalue()).decode()
    pie_chart_html = f'<img src="data:image/png;base64,{pie_chart_base64}" alt="Task Progress Pie Chart">'
    plt.close()
    return pie_chart_html

# Display the response
