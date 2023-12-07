# all required imports
from flask_login import login_user, login_required, current_user, logout_user
from flask_admin.contrib.sqla import ModelView
from flask import Blueprint, render_template, redirect, url_for, request, jsonify, flash, session
from app import app, models, db, admin
from .forms import reviewForm, loginForm, registerForm, albumForm
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask import Flask
import random
from collections import Counter
from collections import defaultdict
from operator import attrgetter



# add admin table views
admin.add_view(ModelView(models.Review, db.session))
admin.add_view(ModelView(models.User, db.session))
admin.add_view(ModelView(models.Albums, db.session))


# home route
@app.route("/", methods=["GET", "POST"])
def home():
    albumsList = models.Albums.query.all()

    if current_user.is_authenticated:
        username = current_user.username
        user_reviews = models.Review.query.filter_by(username=username).all()
        if len(user_reviews) < 3:
            bestGenre = 'None'
            albums = models.Albums.query.all()
        else:
            bestGenre = recomendationAlgorithm(user_reviews, albumsList)
            albums = models.Albums.query.filter_by(genre=bestGenre).all()
    else:
        username = "Guest"
        user_reviews = models.Review.query.all()
        bestGenre = 'None'
        albums = models.Albums.query.all()

    random_album = random.choice(albums)
    album = random_album.title
    artist = random_album.artist

    return render_template("home.html", title="Home", username=username, album = album, artist = artist, bestGenre=bestGenre)

def recomendationAlgorithm(user_reviews, albumsList):
    data = []
    genres = []
    ratingSum = 0
    ratings = []
    genre_ratings = defaultdict(int)

    for review in user_reviews:
        album = review.album
        rating = review.rating
        genre = models.Albums.query.filter_by(title=album).first().genre
        data.append([album, genre, rating])

    for block in data:
        album = block[0]
        genre = block[1]
        rating = block[2]
        
        genres.append(genre)
        ratings.append(rating)

        genre_ratings[genre] += rating

    # find most popular user genre
    genre_counts = Counter(genres)
    most_common_genre = genre_counts.most_common(1)[0][0]
    print(most_common_genre)
    print()

    # find second most popular user genre
    genres.pop(genres.index(most_common_genre))
    genre_counts = Counter(genres)
    most_common_genre = genre_counts.most_common(1)[0][0]
    
    i = 0
    # Print the sum of ratings for each genre
    for genre, rating_sum in genre_ratings.items():
        print(f"Genre: {genre}, Rating Sum: {rating_sum}")
        
        if i == 0:
            ratingSum = (genre,rating_sum)
        else:
            if ratingSum[1] < rating_sum:
                ratingSum = (genre,rating_sum)
        
        i += 1


    return ratingSum[0]
        


    


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
    username = current_user.username
    user_reviews = models.Review.query.filter_by(username=username).all()
    # Sort the reviews based on ratings in descending order
    sorted_reviews = sorted(user_reviews, key=attrgetter('rating'), reverse=True)

    top_reviews = [sorted_reviews[:3]]
    num_valid_reviews = len(top_reviews)
    top_albums = []
    for i in range(num_valid_reviews):
        top_albums.append(top_reviews[0][i].album)
    print(top_albums)

    top_albums2 = []
    for i in range(num_valid_reviews):
        top_albums2.append(models.Albums.query.filter_by(title=top_albums[i]).first())


    return render_template("profile.html", title="Profile", user = user, top_albums= top_albums2)

@app.route("/reviews", methods=["GET", "POST"])
@login_required
def reviews():

    username = current_user.username
    user_reviews = models.Review.query.filter_by(username=username).all()
    return render_template("reviews.html", title="Reviews", reviews=user_reviews)

@app.route("/viewReview/<int:id>", methods=["GET", "POST"])
@login_required
def viewReview(id):

    review = models.Review.query.get(id)

    return render_template("viewReview.html", title="Review", review=review)


@app.route("/explore", methods=["GET", "POST"])
def explore():

    exploreReviews = models.Review.query.all()
    random_reviews = random.sample(exploreReviews, k=10)

    return render_template("explore.html", title="Explore", explore = random_reviews)


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


@app.route("/addAlbum", methods=["GET", "POST"])
@login_required
def addAlbum():

    form = albumForm()

    if form.validate_on_submit():
        p = models.Albums(title=form.title.data, artist=form.artist.data, genre = form.genre.data)
        db.session.add(p)
        db.session.commit()
        return redirect(url_for("reviews"))
    
    return render_template("newAlbum.html", title="New Album", form=form)

