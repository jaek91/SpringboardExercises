from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    """class for website user"""
    __tablename__ = 'user_data'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    first_name = db.Column(db.Text,
                     nullable=False)
    last_name = db.Column(db.Text,
                     nullable=False)

    image_url = db.Column(db.Text, nullable=False, default ="https://freeurlshortener.net/bzZ")

    posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")

    @property
    def full_name(self):
        """Return full name of user"""
        return f"{self.first_name} {self.last_name}"

class Post(db.Model):
    """Class for describing posts"""
    __tablename__ = 'posts'

    id = db.Column(db.Integer,
                   primary_key=True, autoincrement=True)

    title = db.Column(db.Text, nullable=False)

    content = db.Column(db.Text, nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default= datetime.now)

    user_id = db.Column(db.Integer, db.ForeignKey('user_data.id'), nullable = False)

class PostTag(db.Model):
    """Mapping of an tag to a post"""
    __tablename__ = "posts_tags"
    
    post_id = db.Column(db.Integer,
                       db.ForeignKey("posts.id"),
                       primary_key=True)

    tag_id = db.Column(db.Integer,
                       db.ForeignKey("tags.id"),
                       primary_key=True)

class Tag(db.Model):
    """Class for Tag model"""
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.Text, unique = True, nullable=False)

    posts = db.relationship('Post', secondary = "posts_tags",  backref="tags")
