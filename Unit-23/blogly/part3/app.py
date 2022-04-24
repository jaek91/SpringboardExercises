from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post, Tag

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

@app.errorhandler(404)
def page_not_found(e):
    """Show 404 NOT FOUND page."""

    return render_template('404.html'), 404

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

############### Post Routes ###############

@app.route("/users/<int:id>/posts/new", methods=["GET","POST"])
def new_post(id):
    user = User.query.get_or_404(id)
    tags = Tag.query.all()
    if (request.method =="GET"):
        return render_template("posts_show.html", user = user, tags = tags)
    
    if (request.method =="POST"):

        tag_ids = [int(num) for num in request.form.getlist("tags")]
        filtered_tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()

        new_post = Post(
            title = request.form['title'],
            content = request.form['content'],
            user = user ,
            tags = filtered_tags
        )

        db.session.add(new_post)
        db.session.commit()
        
        return redirect(f"/users/{user.id}")

@app.route("/posts/<int:id>")
def show_post(id):
    post = Post.query.get_or_404(id)
    tags = Tag.query.all()
    return render_template("post_details.html", post = post, tags = tags)

@app.route("/posts/<int:id>/edit", methods=["GET","POST"])
def edit_post(id):
    post = Post.query.get_or_404(id)
    tags = Tag.query.all()

    if (request.method =="GET"):
        return render_template("post_edit.html", post = post, tags = tags)
    
    if (request.method =="POST"):
        post.title = request.form["title"]
        post.content = request.form["content"]

        tag_ids = [int(num) for num in request.form.getlist("tags")]
        print(tag_ids)
        for id in tag_ids:
            res = Tag.id.in_(tag_ids)
            print(f"tag-{id} is in tags", res)
        post.tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()

        db.session.add(post)
        db.session.commit()
        return redirect(f"/users/{post.user_id}")

@app.route("/posts/<int:id>/delete", methods=["POST"])
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(f"/users/{post.user_id}")

############### Post and Tag Routes ###############

@app.route("/tags")
def get_all_tags():
    tags = Tag.query.all()
    return render_template("tags_list.html", tags = tags)

@app.route("/tags/<int:id>")
def get_tag(id):
    tag = Tag.query.get_or_404(id)
    return render_template("tags_details.html", tag = tag)

@app.route("/tags/new", methods=["GET","POST"])
def add_new_tags():

    posts = Post.query.all()

    if (request.method =="GET"):
        return render_template("tags_form.html", posts = posts)
     
    if (request.method =="POST"):
        post_ids = [int(num) for num in request.form.getlist("posts")]
        posts = Post.query.filter(Post.id.in_(post_ids)).all()
        new_tag = Tag(name = request.form['tag_name'], posts = posts)

        db.session.add(new_tag)
        db.session.commit()

        return redirect("/tags")

@app.route("/tags/<int:id>/edit", methods=["GET","POST"])
def edit_tags(id):

    tag = Tag.query.get_or_404(id)
    posts = Post.query.all()

    if (request.method == "GET"):
        return render_template("tags_edit.html", tag = tag, posts = posts)

    if (request.method == "POST"):
        tag.name = request.form["tag-name"]
        post_ids = [int(num) for num in request.form.getlist("posts")]
        tag.posts = Post.query.filter(Post.id.in_(post_ids)).all()

        db.session.add(tag)
        db.session.commit()
        return redirect("/tags")

@app.route("/tags/<int:id>/delete", methods=["POST"])
def delete_tag(id):

    tag = Tag.query.get_or_404(id)
    db.session.delete(tag)
    db.session.commit()

    return redirect("/tags")
