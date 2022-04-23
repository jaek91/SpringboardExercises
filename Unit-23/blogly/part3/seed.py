"""Seed file to initialize the db with sample data."""

from models import User, Post, Tag, PostTag, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Post.query.delete()
User.query.delete()

# Add users
Dave = User(first_name='Dave', last_name="Lee")
Jae = User(first_name='Jae', last_name="Kim")
Joe = User(first_name='Joe', last_name="Park")

# Add new objects to session, so they'll persist
## refactor later to add all ****
db.session.add_all([Dave,Jae,Joe])

db.session.flush()

post1 = Post(title="TestPostDave", content="This is a comment for TestPostDave", user_id = Dave.id)
post2 = Post(title="TestPostJae", content="This is a comment for TestPostJae", user_id = Jae.id)
post3 = Post(title="TestPostJoe", content="This is a comment for TestPostJoe", user_id = Joe.id)

db.session.add(post1)
db.session.add(post2)
db.session.add(post3)

db.session.flush()

tag1 = Tag(name="fun")
tag2 = Tag(name="quirky")
tag3 = Tag(name="ordinary")

db.session.add(tag1)
db.session.add(tag2)
db.session.add(tag3)

db.session.flush()

posttag1 = PostTag(post_id = post1.id, tag_id = tag1.id)
posttag2 = PostTag(post_id = post2.id, tag_id = tag2.id)
posttag3 = PostTag(post_id = post3.id, tag_id = tag3.id)

db.session.add(posttag1)
db.session.add(posttag2)
db.session.add(posttag3)

# Commit to the current session
db.session.commit()
