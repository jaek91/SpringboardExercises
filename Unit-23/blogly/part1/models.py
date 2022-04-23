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

    @property
    def full_name(self):
        """Return full name of user"""
        return f"{self.first_name} {self.last_name}"
