from flask import Flask, request
import mysql.connector

app = Flask(__name__)

@app.route('/submit_survey', methods=['POST'])
def submit_survey():
    name = request.form['name']
    stay_duration = request.form['stay_duration']
    booking_method = request.form['booking_method']
    room_satisfaction = request.form['room_satisfaction']
    service_satisfaction = request.form['service_satisfaction']
    comments = request.form['comments']

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database="hotel_survey"
    )

    cursor = db.cursor()

    sql = "INSERT INTO responses (name, stay_duration, booking_method, room_satisfaction, service_satisfaction, comments) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (name, stay_duration, booking_method, room_satisfaction, service_satisfaction, comments)

    cursor.execute(sql, val)

    db.commit()

    return 'Survey submitted successfully!', 200

if __name__ == '__main__':
    app.run(debug=True)
