# GPT-Powered Data Extraction App

This Flask web app lets users input unstructured text and transforms it into structured insights — including a beautiful HTML table and a pie chart — using `gemini-2.0-flash` as the backend LLM.

---

## Features

- 🔍 Extract structured data from free-form text via Gemini 2.0 Flash
- 📊 Display results in both table and pie chart formats
- 🧵 Simple web interface built with Flask
- ⚙️ Modularized logic using helper functions for maintainability

---

## 🧪 Demo Flow

1. User submits text in the form.
2. `text_to_data()` sends it to Gemini for analysis.
3. Response is parsed into a Pandas DataFrame using `gpt_to_df()`.
4. Data is rendered:
   - As an HTML table
   - As a pie chart via `df_to_pie()`

---

## 🧰 Tech Stack

| Layer      | Tools               |
|------------|---------------------|
| Backend    | Flask, Pandas       |
| LLM        | Gemini-2.0-Flash    |
| UI Render  | Bootstrap (via HTML), Matplotlib |
| Deployment | Render  |

---