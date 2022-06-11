import py_compile
import mysql.connector
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/write-data')
def write():
    db = mysql.connector.connect(
        host = "mysql-db-instance.default.svc.cluster.local",
        user = "root",
        passwd = "supersecret",
        database = "company"
    )
    cursor = db.cursor()
    query = "INSERT INTO employees (first_name, last_name, department, email ) VALUES (%s, %s, %s, %s)"
    values = ("Georgi", "Georgiev", "Sales", "g.georgiev@mail.com")
    cursor.execute(query, values)
    db.commit()

    cursor.close()
    return "User has been added"

@app.route('/read-data')
def read():
    db = mysql.connector.connect(
        host = "mysql-db-instance.default.svc.cluster.local",
        user = "root",
        passwd = "supersecret",
        database = "company"
    )
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM employees"
    cursor.execute(query)
    records = cursor.fetchall()
    count = cursor.rowcount
    
    rowCount = range(count)
    dicts = {}
    for i in rowCount:
        for record in records:
            dicts[i+1] = record
    cursor.close()
    
    return dicts
