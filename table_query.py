from upload_data import create_connection


def query_EmailUpload_data():

    # Establish a connection to the SQL Server database
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM [YOURTABLENAME]')
    results = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Pass the results to the HTML template
    return results
