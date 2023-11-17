from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerRangeField, SelectField, PasswordField
from wtforms.validators import DataRequired, ValidationError, Email

class reviewForm(FlaskForm):
    
    title = StringField('Title', validators=[DataRequired()], render_kw={"class": "text-box"})
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
    