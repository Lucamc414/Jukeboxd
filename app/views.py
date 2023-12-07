'''
here all the flask views are handled
'''
import random
from collections import Counter
from collections import defaultdict
from operator import attrgetter
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, current_user, logout_user
from flask_admin.contrib.sqla import ModelView
from flask import render_template, redirect, url_for, request, flash
from app import app, models, db, admin
from .forms import reviewForm, loginForm, registerForm, albumForm





# add admin table views
admin.add_view(ModelView(models.Review, db.session))
admin.add_view(ModelView(models.User, db.session))
admin.add_view(ModelView(models.Albums, db.session))

#home route
@app.route("/", methods=["GET", "POST"])
def home():
    if current_user.is_authenticated:
        username = current_user.username
        user_reviews = models.Review.query.filter_by(username=username).all()
        if len(user_reviews) < 3:
            best_genre = 'None'
            all_albums = models.Albums.query.all()
        else:
            best_genre = recomendation_algorithm(user_reviews)
            all_albums = models.Albums.query.filter_by(genre=best_genre).all()
    else:
        username = "Guest"
        user_reviews = models.Review.query.all()
        best_genre = 'None'
        all_albums = models.Albums.query.all()

    random_album = random.choice(all_albums)
    album = random_album.title
    artist = random_album.artist

    return render_template("home.html", title="Home", username=username,
                            album = album, artist = artist, bestGenre=best_genre)

def recomendation_algorithm(user_reviews):
    data = []
    genres = []
    rating_sum = 0
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

    # find second most popular user genre
    genres.pop(genres.index(most_common_genre))
    genre_counts = Counter(genres)
    most_common_genre = genre_counts.most_common(1)[0][0]
    i = 0
    # Print the sum of ratings for each genre

    for genre, rating_sum in genre_ratings.items():        
        if i == 0:
            rating_tuple= (genre,rating_sum)
        else:
            if rating_tuple[1] < rating_sum:
                rating_tuple = (genre,rating_sum)
        
        i += 1

    return rating_tuple[0]

#login route
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

#register route
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

        new_user = models.User(email=email, username=username,password=password,
                                profile_photo=profile_photo)

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template("register.html", title="Login", form=form)

#logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

#profile route
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

#reviews route
@app.route("/reviews", methods=["GET", "POST"])
@login_required
def reviews():

    username = current_user.username
    user_reviews = models.Review.query.filter_by(username=username).all()
    return render_template("reviews.html", title="Reviews", reviews=user_reviews)

#view review route
@app.route("/viewReview/<int:identifier>", methods=["GET", "POST"])
@login_required
def view_review(identifier):

    review = models.Review.query.get(identifier)

    return render_template("viewReview.html", title="Review", review=review)

#explore route
@app.route("/explore", methods=["GET", "POST"])
def explore():

    explore_reviews = models.Review.query.all()
    random_reviews = random.sample(explore_reviews, k=10)

    return render_template("explore.html", title="Explore", explore = random_reviews)

#albums route
@app.route("/albums", methods=["GET", "POST"])
def albums():
    albums_list = models.Albums.query.all()
    return render_template("albums.html", title="Albums", albums=albums_list)

#new review route
@app.route("/newReview", methods=["GET", "POST"])
def new_review():
   
    form = reviewForm()
    username = current_user.username

    if form.validate_on_submit():
        title = form.album.data
        artist = models.Albums.query.filter_by(title=title).first().artist

        entry = models.Review(title=form.title.data, artist = artist,
                               review = form.review.data,
                           rating = form.rating.data, username=username, album=form.album.data)
       
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for("reviews"))
  
    return render_template("newReview.html", title="New Review", form=form, username=username)

#new album route
@app.route("/addAlbum", methods=["GET", "POST"])
@login_required
def add_album():

    form = albumForm()

    if form.validate_on_submit():
        entry = models.Albums(title=form.title.data, artist=form.artist.data,
                              genre = form.genre.data)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for("reviews"))
   
    return render_template("newAlbum.html", title="New Album", form=form)
