from flask import Flask, render_template, request
import pandas as pd
from upload_data import upload_data_to_sql_server
from table_query import query_EmailUpload_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Get the uploaded file from the request object
    excel_file = request.files['file']

    try:
        # Read the file into a pandas dataframe
        df = pd.read_excel(excel_file, sheet_name=0)

        # Upload the data to SQL Server
        upload_data_to_sql_server(df)

        # Redirect back to the home page with a success message
        message = 'The file has been successfully uploaded in the database.'
        return render_template('index.html', message=message)

    except Exception as e:
        # Handle any exceptions raised during the upload process and pass a failure message to the template
        message = 'Upload failed. Please upload the excel file with all columns populated.'
        return render_template('index.html', message=message)
    
@app.route('/', methods=['POST'])
def show_table():
    # Get the results of the SQL query
    results = query_EmailUpload_data()

    # Pass the results to the HTML template
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)