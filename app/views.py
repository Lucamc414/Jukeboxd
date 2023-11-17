# all required imports
from flask import render_template, redirect, url_for, request, jsonify, flash
from app import app, models, db, admin
from .forms import reviewForm, loginForm, registerForm
from flask_admin.contrib.sqla import ModelView

# add admin table views
admin.add_view(ModelView(models.Review, db.session))
admin.add_view(ModelView(models.User, db.session))
admin.add_view(ModelView(models.Song, db.session))


# home route
@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html", title="Home")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = loginForm()
    return render_template("login.html", title="Login", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = registerForm()
    return render_template("register.html", title="Login", form=form)

@app.route("/reviews", methods=["GET", "POST"])
def reviews():
    return render_template("reviews.html", title="Reviews" ,reviews=models.Review.query.all())

@app.route("/explore", methods=["GET", "POST"])
def explore():
    return render_template("explore.html", title="Explore")

@app.route("/newReview", methods=["GET", "POST"])
def newReview():
    
    form = reviewForm()

    if form.validate_on_submit():
        print('here')
        p = models.Review(title=form.title.data, artist=form.artist.data, review = form.review.data, rating = form.rating.data)
        db.session.add(p)
        db.session.commit()
        return redirect(url_for("reviews"))
    
    return render_template("newReview.html", title="New Review", form=form)




