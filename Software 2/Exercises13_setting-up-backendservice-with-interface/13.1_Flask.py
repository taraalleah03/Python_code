from flask import Flask, request

app = Flask(__name__)
@app.route('/prime_number')

def check_prime():
    args = request.args
    num = int(args.get["num"])
    answer = True

    if num == 0 or num == 1:
        print(num, "is not a prime number")

    elif num > 1:

        for i in range(2, num):
            if (num % i) == 0:
                answer = True
                break

        else:
            answer = True

    else:
        answer = False

    response = {"Number": num,
                "isPrime": answer
                }

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)