import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


APP = Flask (__name__)


APP.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
APP.config["MONGO_URI"] = os.environ.get("MONGO_URI")
APP.secret_key = os.environ.get("SECRET_KEY")


# Global Variables:
MONGO = PyMongo(APP)
reviews = MONGO.db.reviews
genres = MONGO.db.genre
users =  MONGO.db.users


# About page route
@APP.route("/")
def about():
    return render_template("pages/about.html")


# Search functionality in discovery page
@APP.route("/search", methods=["GET", "POST"])
def search_discover():
    query = request.form.get("query")
    reviews = list(MONGO.db.reviews.find({"$text": {"$search": query}}))
    return render_template("pages/discover.html", reviews=reviews)


# Add review function
@APP.route("/add/review", methods={"GET", "POST"})
def add_review():
    if request.method == "POST":
        review = {
            "title": request.form.get("title"),
            "author": request.form.get("author"),
            "genre": request.form.get("genre_category"),
            "length": request.form.get("length"),
            "ease_of_reading": request.form.get("ease_of_reading"),
            "plot_summary": request.form.get("plot_summary"),
            "favorite_quote": request.form.get("favorite_quote"),
            "rating": request.form.get("rating"),
            "link_to_image": request.form.get("link_to_image"),
            "link_to_buy": request.form.get("link_to_buy"),
            "reviewed_by": session["user"]
        }
        reviews.insert_one(review)
        # Flash message
        flash("review added")
        return redirect(url_for("user_reviews"))

    genre = genres.find().sort("genre_category", 1)
    # My-reviews template is rendered using add_review template as main content
    return render_template("pages/my-reviews.html", main_content="add_review", genre=genre)


# Edit review function 
@APP.route("/edit/review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    if request.method == "POST":
        submit = {"$set": {
            "title": request.form.get("title"),
            "author": request.form.get("author"),
            "genre": request.form.get("genre_category"),
            "length": request.form.get("length"),
            "ease_of_reading": request.form.get("ease_of_reading"),
            "plot_summary": request.form.get("plot_summary"),
            "favorite_quote": request.form.get("favorite_quote"),
            "rating": request.form.get("rating"),
            "link_to_image": request.form.get("link_to_image"),
            "link_to_buy": request.form.get("link_to_buy")
            }
        }
        reviews.update_one({"_id": ObjectId(review_id)}, submit)
        # Flash message 
        flash("review updated!")
        return redirect(url_for("user_reviews"))   
        
    review = reviews.find_one({"_id": ObjectId(review_id)})
    genre = genres.find().sort("genre_category", 1)
    # My-reviews template is rendered using edit_review template as main content
    return render_template("pages/my-reviews.html", main_content="edit_review", review=review, genre=genre)
    

# Delete function 
@APP.route("/delete/review/<review_id>")
def delete_review(review_id):
    reviews.delete_one({"_id": ObjectId(review_id)})
    # Flash message
    flash("Review Deleted")
    return redirect(url_for("user_reviews"))


# My reviews function displaying each user their own reviews
@APP.route("/my/reviews", methods=["GET", "POST"])
def user_reviews():
    if session["user"]:
        user_profile = users.find_one({"username": session["user"]})
        reviews = list(MONGO.db.reviews.find({"reviewed_by": session["user"]}))
        return render_template("pages/my-reviews.html", user=user_profile, reviews=reviews)
    return redirect(url_for("user_reviews"))


# Discover reviews function displaying all the reviews that exist in DB
@APP.route("/discover/reviews", methods=["GET"])
def discover():
    if request.method == "GET":
        reviews = MONGO.db.reviews.find().sort("genre")
        return render_template("pages/discover.html", reviews=reviews)
    return redirect(url_for("discover"))


# Function allowing users to add items to their favorites template
@APP.route("/add/favorites/<review_id>")
def add_favorites(review_id):
    if session["user"]:
        # check if favorite already exists
        favorite_review_exists = users.find_one(session["user"], {"favorites": ObjectId(review_id)})
        if favorite_review_exists: 
            # Flash message to announce existing item in favorites
            flash("this review is already in your favorites")
            return redirect(url_for("discover"))
        # if doesn't exist, it adds the review to DB
        user_profile = users.find_one({'username': session['user'].lower()})
        users.update(user_profile, {"$push": {"favorites": ObjectId(review_id)}})
        # Flash message
        flash("Review added to favorites")
        return redirect(url_for('discover'))
        
    return redirect(url_for('discover'))


# Delete items from favorites template
@APP.route('/delete/favorites/<review_id>')
def delete_favorites(review_id):
    user_profile = users.find_one({'username': session['user'].lower()})
    users.update(user_profile, {"$pull": {"favorites": ObjectId(review_id)}})
    # Flash message
    flash("Review removed from favorites")
    return redirect(url_for('user_favorites'))


# Function to render favorites template for every user
""" 
This function idea was borrowed from:
https://github.com/Geomint/beer-time/blob/master/APP.py 
"""
@APP.route("/user/favorites", methods=["GET", "POST"])
def user_favorites():
    user_profile = users.find_one({'username': session['user'].lower()})
    user_profile_fav = user_profile['favorites']
    fav_review = []
    fav_review_id = []

    if len(user_profile['favorites']) != 0:
        for fav in user_profile_fav:
            review = reviews.find_one({'_id': fav})
            review_id = review['_id']
            fav_review_id.APPend(review_id)

    for fav in user_profile_fav:
        review = reviews.find_one({'_id': fav})
        fav_review.APPend(review)

    return render_template("pages/favorites.html", fav_review_id=fav_review_id,
                           fav_review=fav_review, user_profile=users.find_one(
                               {'username': session['user'].lower()}))


# User registration
@APP.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in database
        existing_user = users.find_one(
            { "username": request.form.get("username").lower()})
        # if the user exists - it flashes a message
        if existing_user:
            # Flash message
            flash("Username already exists")
            return redirect(url_for("register"))
        
        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "favorites": []
        }
        users.insert_one(register)
        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        # Flash message
        flash("Welcome, {}".format(
                        request.form.get("username")))
        return redirect(url_for("discover", username=session["user"]))
    # Access template renders with register form as main content
    return render_template("pages/access.html", main_content="register")


# User login
@APP.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in database
        existing_user = users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user: 
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    # Flash message
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "discover", username=session["user"]))
            else: 
                # invalid password match
                return redirect(url_for("login"))
        else: 
            # username doesn't exist
            return redirect(url_for("login"))
        return redirect(url_for("login"))
    # Access template renders with login form as main content
    return render_template("pages/access.html", main_content="login")


# User logout
@APP.route("/logout")
def logout():
    # remove user from session cookies
    session.pop("user")
    return redirect(url_for("login"))


# Function to render profile template
@APP.route("/profile", methods=["GET", "POST"])
def profile():
    if session["user"]:
        # grab the session user's credentials from database
        user_profile = users.find_one({"username": session["user"]})
        return render_template("pages/profile.html", user=user_profile)
    return redirect(url_for("login"))


# Function to edit profile
@APP.route("/edit/profile/<user_profile_id>", methods=["GET", "POST"])
def edit_profile(user_profile_id):
    if request.method == "POST":
        submit = {"$set": {
            "username": request.form.get("username"), 
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password"))
            }
        }
        users.update_one({"_id": ObjectId(user_profile_id)}, submit)
        #update user session to push new username before re-directing
        session["user"] = request.form.get("username")
        #Flash message
        flash("User Profile Successfully Updated!")
        return redirect(url_for("profile"))
        
    user_profile = users.find_one({"_id": ObjectId(user_profile_id)})
    # Profile template is rendered using edit_profile template as main content
    return render_template("pages/profile.html", main_content="edit_profile", user=user_profile)


# error 404 page
@APP.errorhandler(404)
def page_not_found(error):
    error = str(error)
    return render_template('pages/404.html', error=error), 404


if __name__ == "__main__":
    APP.run(host=os.environ.get("IP"), 
            port=int(os.environ.get("PORT")), 
            debug=os.environ.get("DEBUG"))
