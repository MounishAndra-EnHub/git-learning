from flask import Flask, request, render_template
import pymysql
import os

app = Flask(__name__)

# Cloud SQL connection settings
DB_HOST = os.environ.get("DB_HOST", "34.122.118.166")
DB_USER = os.environ.get("DB_USER", "mounish")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "root")
DB_NAME = os.environ.get("DB_NAME", "storedata")

def get_db_connection():
    return pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
        conn.close()
        return "Data submitted!"
    return render_template("form.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
