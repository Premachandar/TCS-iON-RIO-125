from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/data')
def data():
    db = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="hotel_survey"
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM responses")

    data = cursor.fetchall()

    return jsonify(data)
