from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        conn = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST', 'db'),
            user=os.getenv('MYSQL_USER', 'root'),
            password=os.getenv('MYSQL_PASSWORD', 'root'),
            database=os.getenv('MYSQL_DATABASE', 'testdb')
        )
        return "Flask connected successfully to MySQL! - v2.0"
    except Exception as e:
        return f"Database connection failed: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)