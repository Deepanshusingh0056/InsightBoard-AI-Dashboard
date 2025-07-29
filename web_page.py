
html = '''
<!doctype html>
<html>
  <head><title>Data Extractor</title></head>
  <body>
    <h2>Enter a String:</h2>
    <form method="POST">
      <input type="text" name="user_input" required>
      <input type="submit" value="Submit">
    </form>
    {% if submitted %}
    <p>You entered: {{ user_input }}</p>
    {% if table_html %}
        <h3>📋 Extracted Data</h3>
        {{ table_html | safe }}
    {% else %}
    
        <p>No data extracted.</p>
    {% endif %}
    <h3>📊 Task Progress</h3>
    {{ pie_chart_html | safe }}
    {% endif %}
  </body>
</html>
'''