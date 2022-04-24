"""Seed file to make sample data for user db."""

from models import User, db

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add users
Dave = User(first_name='Dave', last_name="Lee")
Jae = User(first_name='Jae', last_name="Kim")
Joe = User(first_name='Joe', last_name="Park")

# Add new objects to session, so they'll persist

db.session.add_all([Dave,Jae,Joe])

# Commit to the current session
db.session.commit()
