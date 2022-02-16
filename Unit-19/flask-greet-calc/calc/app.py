# Put your app in here.
from flask import Flask, request
from operations import *


app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the Home Page!"

@app.route("/add")
def add_values():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = add(a,b)
    return f"the sum of {a} and {b} is {res}"

@app.route("/sub")
def subtract_values():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = sub(a,b)
    return f"the difference of {a} and {b} is {res}"

@app.route("/mult")
def mult_values():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = mult(a,b)
    return f"the product of {a} and {b} is {res}"

@app.route("/div")
def div_values():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = div(a,b)
    return f"the quotient of {a} and {b} is {res}"







