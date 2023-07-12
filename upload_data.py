import pyodbc

def create_connection():
    server = 'YourServerName'
    database = 'YourDatabaseName'
    username = 'Username'
    password = 'Password'
    driver = '{ODBC Driver 17 for SQL Server}'

    # Create connection string using connection parameters
    conn_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"

    # Create database connection using pyodbc
    conn = pyodbc.connect(conn_string)
    
    return conn

def upload_data_to_sql_server(df):

    conn = create_connection()
    insert_table_name = '[YourTableName]'

    # Create SQL query to insert data into SQL Server table by checking if all columns are present
    columns = [col for col in df.columns if col in {'Column0Heading', 'Column1Heading', 'Column2Heading', 'Column3Heading', 'Column4Heading'}]
    placeholders = ', '.join('?' for _ in columns)
    columns_str = ','.join(columns)
    sql_query = f"INSERT INTO {insert_table_name} ({columns_str}) VALUES ({placeholders})"

    # Use pyodbc to execute the SQL query with a list of parameters for each row in the dataframe
    cursor = conn.cursor()
    for _, row in df.iterrows():
        values = [row[col] if col in row.index and pd.notnull(row[col]) else '' for col in columns]
        cursor.execute(sql_query, tuple(values))

    # Commit the changes
    conn.commit()
