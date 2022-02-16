from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "You are here at the main page"

@app.route("/welcome")
def welcome_greet():
    return "welcome"

@app.route("/welcome/home")
def welcome_home_greet():
    return "welcome home"

@app.route("/welcome/back")
def welcome_back_greet():
    return "welcome back"

    