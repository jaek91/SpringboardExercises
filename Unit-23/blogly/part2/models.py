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

