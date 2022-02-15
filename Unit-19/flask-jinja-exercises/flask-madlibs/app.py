from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret-stuff"
debug = DebugToolbarExtension(app)

@app.route('/')
def show_form():
    """routes user to the main page of forms to input words"""
    story_prompts = story.prompts
    return render_template("form.html", prompts = story_prompts)

@app.route("/story")
def show_story():
    """handles the story that's going to be shown to the user when it hits this route """
    story_text = story.generate(request.args)
    return render_template("story.html", text = story_text)