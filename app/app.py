import pyodbc
from flask import Flask

app = Flask(__name__, static_url_path=static_url_path)
conn_data = {
    'hostname': 'hostname',
    'username': 'username',
    'password': 'password',
    'database': 'database'
}

@app.route('/', methods=['GET'])
def index():  # pragma: no cover
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 13 for SQL Server};SERVER=' + conn_data['hostname'] + ';PORT=1443;UID=' +
        conn_data['username'] + ';PWD=' + conn_data['password'] + ';DATABASE=' + conn_data['database'])

    cursor = cnxn.cursor()

    cursor.execute("select * from table")
    row = cursor.fetchone()
    print("ID: {}, NAME: {}, Data Exclusao: {}, Intent: {}".format(row.id, row.name))

