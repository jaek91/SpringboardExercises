"""Seed file to make sample data for user db."""

from models import User, Post, db

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

db.session.add_all([Dave,Jae,Joe])

db.session.flush()

post1 = Post(title="TestPostDave", content="This is a comment for TestPostDave", user_id = Dave.id)
post2 = Post(title="TestPostJae", content="This is a comment for TestPostJae", user_id = Jae.id)
post3 = Post(title="TestPostJoe", content="This is a comment for TestPostJoe", user_id = Joe.id)

db.session.add_all([post1,post2,post3])
# Commit to the current session
db.session.commit()
