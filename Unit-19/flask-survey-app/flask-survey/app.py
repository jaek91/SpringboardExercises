from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)

app.config['SECRET_KEY'] = "clearly_secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


@app.route("/")
## show title of the survey, the instructions, and a button to start the survey
def show_survey():
    return render_template("survey-start.html", survey = satisfaction_survey)

@app.route("/start", methods=["POST"])
def redirect_to_question():
    session["responses"] = []
    return redirect("/questions/0")

@app.route("/questions/<int:qid>")
def display_question(qid):

    responses = session.get("responses")     

    if (len(responses) == len(satisfaction_survey.questions)):
        ## if all questions have been answered, direct them to thank you page
        return redirect("/survey-complete")
    if (len(responses) != qid):
        flash("You've entered an invalid question url!")
        return redirect(f"/questions/{len(responses)}")

    survey_question = satisfaction_survey.questions[qid]

    return render_template("questions.html", question_num= qid, survey_question = survey_question)

@app.route("/answer", methods=["POST"])
def route_answer():
    ##extract the user choice from the question
    user_answer = request.form["answer"]

    ##then store in the session
    responses = session["responses"]
    responses.append(user_answer)
    session["responses"] = responses

    if(len(responses) == len(satisfaction_survey.questions)):
        return redirect("/survey-complete")
    else: 
        return redirect(f"/questions/{len(responses)}") 
    
    

@app.route("/survey-complete")
def show_thanks():
    return render_template("survey-completed.html")