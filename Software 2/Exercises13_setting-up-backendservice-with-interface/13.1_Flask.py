from flask import Flask, request, json, jsonify

app = Flask(__name__)
@app.route('/prime_number/<int:num>')

def check_prime(num):
    answer = True

    if num == 0 or num == 1:
        answer = False

    else:

        for i in range(2, num):
            if (num % i) == 0:
                answer = False
                break

    response = {"Number": num,
                "isPrime": answer
                }

    return jsonify(response)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)