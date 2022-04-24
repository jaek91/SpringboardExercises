from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  =  False
app.config['SQLALCHEMY_ECHO'] =  True
app.config['SECRET_KEY'] = 'Secret-key-for-flask'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def init():
    """Shows initial list of all users in db"""
    return redirect("/users")

@app.route("/users")
def show_init_users():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route("/users/new", methods=["GET","POST"])
def new_users():
    if (request.method =="GET"):
        return render_template("user_form.html")
    if (request.method =="POST"):
        new_user = User(
            first_name = request.form['first_name'],
            last_name = request.form['last_name'],
            image_url = request.form['image_url'] or None
            )
       
        db.session.add(new_user)
        db.session.commit()
        return redirect('/users')

@app.route("/users/<int:id>")
def show_users(id):
    user = User.query.get_or_404(id)
    return render_template('user_profile.html', user=user)

@app.route("/users/<int:id>/edit", methods=["GET","POST"])
def edit_user(id):
    user = User.query.get_or_404(id)
    if (request.method =="GET"):
        return render_template('user_edit_form.html', user=user)
    
    if (request.method =="POST"):
        user.first_name = request.form['first_name']
        user.last_name = request.form['last_name']
        user.image_url = request.form['image_url'] 

        db.session.add(user)
        db.session.commit()
        return redirect('/users')

@app.route("/users/<int:id>/delete", methods=["POST"])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/users')
