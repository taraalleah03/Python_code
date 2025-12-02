from flask import Flask, jsonify
import mariadb

app = Flask(__name__)

connection = mariadb.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='taRamart!n2003thirty',
    database='flight_game',
    autocommit=True)

@app.route('/airport/<ICAO>')
def airport(ICAO):
    cursor = connection.cursor()

    cur