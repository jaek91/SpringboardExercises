from flask import Flask, request, render_template, jsonify, session
from boggle import Boggle


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret-key"

boggle_game = Boggle()

@app.route("/")
def index():
    """Shows content on homepage"""
    board = boggle_game.make_board()
    session["board"] = board
    highscore = session.get("highscore",0)
    numplays = session.get("numplays",0)

    return render_template("home.html", board = board, highscore = highscore, numplays = numplays)

@app.route("/check-word", methods=["GET"])
def word_validate():
    """checks if a word is on board and then returns the json result"""
    board = session["board"]
    word = request.args["word"]
    response = boggle_game.check_valid_word(board, word)
    return jsonify({"result": response})

@app.route("/post-score", methods =["POST"])
def show_score():
    """keeps track of the score, high score and number of games played and displays their information"""
    score = request.json["score"]
    highscore = session.get("highscore", 0)
    numplays = session.get("numplays", 0)
    
    session["numplays"] = numplays + 1
    session["highscore"] = max(score, highscore)

    newRecord = score > highscore

    return jsonify(newRecord)
