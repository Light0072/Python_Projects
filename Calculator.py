from flask import Flask, request, render_template
import numpy as np
import matplotlib.pyplot as plt
import os
import random


def pretty_print(f, degree):
    L = []
    s = ""
    for i in range(len(f)):
        n = degree - i
        if n == 0:
            L.append(str(f[i]))
        if n == 1:
            L.append(str(f[i]) + "*x")
        if n > 1:
            L.append(str(f[i]) + "*x^" + str(n))
    print(L)
    for i in range(len(L)):
        if '-' in L[i][0]:
            s = s + L[i]
        else:
            s = s + "+" + L[i]
    if s[0] == '+':
        return s[1:len(s)]
    else:
        return s


def polynomial_fit(L1, L2, degree):
    x = np.array(L1)
    y = np.array(L2)
    f = np.polyfit(x, y, degree).round(decimals=2)
    return pretty_print(f, degree), x, y, f


def process_input(s):
    return eval(s)


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('application.html')


@app.route('/', methods=['POST'])
def request_data():
    X = process_input(request.form['text1'])
    Y = process_input(request.form['text2'])
    d = process_input(request.form['text3'])
    P, x, y, f = polynomial_fit(X, Y, d)  # text1.upper()

    return render_template('application.html', result=P, x_values=x, y_values=y)


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, use_reloader=True)
