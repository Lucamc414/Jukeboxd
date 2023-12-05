# all required imports
from flask_login import login_user, login_required, current_user, logout_user
from flask_admin.contrib.sqla import ModelView
from flask import Blueprint, render_template, redirect, url_for, request, jsonify, flash, session
from app import app, models, db, admin
from .forms import reviewForm, loginForm, registerForm
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask import Flask
import random
import os
import tkinter as tk
from tkinter import messagebox



# add admin table views
admin.add_view(ModelView(models.Review, db.session))
admin.add_view(ModelView(models.User, db.session))
admin.add_view(ModelView(models.Albums, db.session))


# home route
@app.route("/", methods=["GET", "POST"])
def home():
    if current_user.is_authenticated:
        username = current_user.username
    else:
        username = "Guest"


    albumsList = models.Albums.query.all()
    album = random.choice(albumsList)


    return render_template("home.html", title="Home", username=username, album = album)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = loginForm()

    if form.validate_on_submit():
        user = models.User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=True)
                return redirect(url_for("home"))
            else:
                flash("Invalid Password")
        else:
            flash("Invalid Username")

    return render_template("login.html", title="Login", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():

    form = registerForm()

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        #profile_photo = request.files['profile_picture']
        profile_photo = 'app/static/profile.png'


        user = models.User.query.filter_by(email=email).first()

        if user:
            flash('Email address already exists')
            return redirect(url_for("register"))
        
        password = generate_password_hash(password, method='pbkdf2:sha256')

        # Save the profile photo to a specific location

        #profile_photo.save(os.path.join(app.config['UPLOAD_FOLDER'], profile_photo))

        new_user = models.User(email=email, username=username,password=password, profile_photo=profile_photo)

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template("register.html", title="Login", form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/profile')
@login_required
def profile():

    user = models.User.query.filter_by(username=current_user.username).first()
    return render_template("profile.html", title="Profile", user = user)

@app.route("/reviews", methods=["GET", "POST"])
@login_required
def reviews():

    username = current_user.username
    user_reviews = models.Review.query.filter_by(username=username).all()
    return render_template("reviews.html", title="Reviews", reviews=user_reviews)

@app.route("/explore", methods=["GET", "POST"])
def explore():

    exploreReviews = models.Review.query.all()

    return render_template("explore.html", title="Explore", explore = exploreReviews)

@app.route("/albums", methods=["GET", "POST"])
def albums():

    albums = models.Albums.query.all()

    return render_template("albums.html", title="Albums", albums=albums)

@app.route("/newReview", methods=["GET", "POST"])
def newReview():
    
    form = reviewForm()
    username = current_user.username

    if form.validate_on_submit():
        print('here')
        p = models.Review(title=form.title.data, artist=form.artist.data, review = form.review.data, rating = form.rating.data, username=username, album=form.album.data)
        db.session.add(p)
        db.session.commit()
        return redirect(url_for("reviews"))
    
    return render_template("newReview.html", title="New Review", form=form, username=username)




