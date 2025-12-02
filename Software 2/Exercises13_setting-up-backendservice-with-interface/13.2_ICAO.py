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

@app.route('/airport/<ident>', strict_slashes=False)
def airport(ident):
    cursor = connection.cursor()
    cursor.execute("SELECT name, municipality FROM airport WHERE ident = ?", (ident,))
    result = cursor.fetchone()
    cursor.close()

    if result:
        name, municipality = result
        response = {
            'Ident': ident, #There doesn't seem to be an ICAO in our existing DB
            'Name': name,
            'Location': municipality,
        }
    else:
        response = {
            'Error': 'Invalid identifier',
        }

    return jsonify(response)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)