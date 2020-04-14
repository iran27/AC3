import os
from flask import Flask, jsonify, request
from math import sqrt


app = Flask(__name__)


@app.route('/')
def cemprimos():
    limite = 99

    c = 1
    p = 1
    numero = 3

    primos = "2,"

    while p < limite:
        ehprimo = 1
        for i in range(2, numero):
            ehprimo = 0
            break
        if (ehprimo):
            primos = primos + str(numero)
            p += 1
        numero += 1

    return primos


if __name__ == "_main_":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
