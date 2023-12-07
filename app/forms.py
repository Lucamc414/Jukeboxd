from flask_wtf.file import FileAllowed
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerRangeField, SelectField, PasswordField,FileField
from wtforms.validators import DataRequired, ValidationError, Email 

from app import models, app

class reviewForm(FlaskForm):
    
    title = StringField('Title', validators=[DataRequired()], render_kw={"class": "text-box"})
    choicesList =[]
    with app.app_context():
        albumsList = [album.title for album in models.Albums.query.all()]

        for album in albumsList:
            #get artist of album
            artist = models.Albums.query.filter_by(title=album).first().artist
            choicesList.append((album, f"{album} - {artist}"))

        album = SelectField('Album',choices= choicesList, validators=[DataRequired()])

    artist = StringField('Artist', validators=[DataRequired()], render_kw={"class": "text-box"})
    review = StringField('Review', validators=[DataRequired()], render_kw={"class": "text-box review-box"})
    rating = SelectField('Rating', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], validators=[DataRequired()])



class loginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={"class": "text-box", "autocomplete": "off"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"class": "text-box"})

class registerForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"class": "text-box"})
    username = StringField('Username', validators=[DataRequired()], render_kw={"class": "text-box", "autocomplete": "off"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"class": "text-box"})
    passwordConfirm = PasswordField('PasswordConfirm', validators=[DataRequired()], render_kw={"class": "text-box"})
    profile_picture = FileField('Profile Picture', validators=[DataRequired(), FileAllowed(['jpg', 'jpeg', 'png'])])

class albumForm(FlaskForm):
    title = StringField('Album Title', validators=[DataRequired()], render_kw={"class": "text-box"})
    artist = StringField('Artist/ Band', validators=[DataRequired()], render_kw={"class": "text-box"})
    genre = StringField('Genre', validators=[DataRequired()], render_kw={"class": "text-box"})