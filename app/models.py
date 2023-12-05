from app import db
from flask_login import UserMixin

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), index=True)
    artist = db.Column(db.String(50), index=True)
    review = db.Column(db.String(500), index=True)
    rating = db.Column(db.Integer, index=True)
    album = db.Column(db.String(50), index=True)
    username = db.Column(db.String(50), index=True)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True)
    password = db.Column(db.String(50), index=True)
    email = db.Column(db.String(50), index=True)
    profile_photo = db.Column(db.String(100), index=True)


class Albums(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), index=True)
    artist = db.Column(db.String(50), index=True)
    genre = db.Column(db.String(50), index=True)
