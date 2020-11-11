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


@APP.route("/")
def about():
    """
    About page route.
    """
    return render_template("pages/about.html")


@APP.route("/search", methods=["GET", "POST"])
def search_discover():
    """
    Search functionality in discover page
    that allows the users to search any text
    displayed on the page.
    """
    query = request.form.get("query")
    reviews = list(MONGO.db.reviews.find(
        {"$text": {"$search": query}}))
    return render_template("pages/discover.html",
    reviews=reviews)


@APP.route("/add/review", methods={"GET", "POST"})
def add_review():
    """
    Add review function allows to store user input into
    the database.It also renders my-reviews page using
    add_review as main content.
    """
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
        flash("review added")
        return redirect(url_for("user_reviews"))

    genre = genres.find().sort("genre_category", 1)
    return render_template("pages/my-reviews.html", 
    main_content="add_review", genre=genre)


@APP.route("/edit/review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    """
    Edit review function allows the user
    to edit their existing template 
    by fetching the data from DB. 
    It also renders my-reviews template 
    using edit_review as main content. 
    """
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
        flash("review updated!")
        return redirect(url_for("user_reviews"))   
        
    review = reviews.find_one({"_id": ObjectId(review_id)})
    genre = genres.find().sort("genre_category", 1)
    return render_template("pages/my-reviews.html", 
    main_content="edit_review", review=review, genre=genre)
    

@APP.route("/delete/review/<review_id>", methods=["GET", "POST"])
def delete_review(review_id):
    """
    Delete function allows the user 
    to remove their own reviews
    one at a time.
    """ 
    reviews.delete_one({"_id": ObjectId(review_id)})
    flash("Review Deleted")
    return redirect(url_for("user_reviews"))


@APP.route("/my/reviews", methods=["GET", "POST"])
def user_reviews():
    """
    My reviews function displays each user
    their own reviews. It renders in my-reviews page.
    """
    if session["user"]:
        user_profile = users.find_one(
            {"username": session["user"]})
        reviews = list(MONGO.db.reviews.find(
            {"reviewed_by": session["user"]}))
        return render_template("pages/my-reviews.html", 
        user=user_profile, reviews=reviews)
    return redirect(url_for("user_reviews"))


@APP.route("/discover/reviews")
def discover():
    """
    Discover reviews function displays
    all of the reviews that exist in DB
    and renders discover page.
    """
    reviews = MONGO.db.reviews.find().sort("genre")
    return render_template("pages/discover.html",
    reviews=reviews)


@APP.route("/add/favorites/<review_id>", methods=["GET", "POST"])
def add_favorites(review_id):
    """
    Function allowing users to add items to their
    favorites template. First, it checks if the 
    favorite already exists and if it doesn't
    then it add to the collection.
    """
    if session["user"]:
        current_user = {'username': session['user'].lower()}
        favorite_reviews = users.find_one(current_user)["favorites"]
        if ObjectId(review_id) in favorite_reviews:
            flash("this review is already in your favorites")
            return redirect(url_for("discover"))
        user_profile = users.find_one(
            {'username': session['user'].lower()})
        users.update(user_profile,
        {"$push": {"favorites": ObjectId(review_id)}})
        flash("Review added to favorites")
        return redirect(url_for('discover'))
        
    return redirect(url_for('discover'))


@APP.route('/delete/favorites/<review_id>')
def delete_favorites(review_id):
    """
    Delete items from favorites template. 
    The function finds the session user first,
    then removed the entry from DB.
    """
    user_profile = users.find_one(
        {'username': session['user'].lower()})
    users.update(user_profile, 
    {"$pull": {"favorites": ObjectId(review_id)}})
    flash("Review removed from favorites")
    return redirect(url_for('user_favorites'))


@APP.route("/user/favorites")
def user_favorites():
    """
    This function idea was borrowed from:
    https://github.com/Geomint/beer-time/blob/master/app.py
    It renders favorite template for every user.
    """
    user_profile = users.find_one(
        {'username': session['user'].lower()})
    user_profile_fav = user_profile['favorites']
    fav_review = []
    fav_review_id = []

    if len(user_profile['favorites']) != 0:
        for fav in user_profile_fav:
            review = reviews.find_one({'_id': fav})
            review_id = review['_id']
            fav_review_id.append(review_id)

    for fav in user_profile_fav:
        review = reviews.find_one({'_id': fav})
        fav_review.append(review)

    return render_template("pages/favorites.html",
    fav_review_id=fav_review_id,
    fav_review=fav_review, user_profile=users.find_one(
    {'username': session['user'].lower()}))


@APP.route("/register", methods=["GET", "POST"])
def register():
    """
    Function allowing new user registration.
    It first checks if the user already exists based on the username,
    if it doesn't it stores the data in DB, 
    and also adds to cookie. 
    As a result it renders access.html with register
    as main content. 
    """
    if request.method == "POST":
        existing_user = users.find_one(
            { "username": request.form.get("username").lower()})
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        
        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(
                request.form.get("password")),
            "favorites": []
        }
        users.insert_one(register)
        session["user"] = request.form.get("username").lower()
        flash("Welcome, {}".format(
                        request.form.get("username")))
        return redirect(url_for("discover", username=session["user"]))
    return render_template("pages/access.html", main_content="register")


@APP.route("/login", methods=["GET", "POST"])
def login():
    """
    Function that allows the user to login. 
    It checks if the users exists in the DB, 
    then checks if entered password is correct. If the username or
    password doesn't match it won't allow to login. 
    Else it renders access page with login as main content.
    """
    if request.method == "POST":
        existing_user = users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user: 
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "discover", username=session["user"]))
            else: 
                return redirect(url_for("login"))
        else: 
            return redirect(url_for("login"))
        return redirect(url_for("login"))
    return render_template("pages/access.html", main_content="login")


@APP.route("/logout")
def logout():
    """ 
    remove user from session cookies 
    """
    session.pop("user")
    return redirect(url_for("login"))


@APP.route("/profile")
def profile():
    """
    Function to render profile template. It gets
    user's credentials from DB and renders 
    profile page.
    """
    if session["user"]:
        user_profile = users.find_one(
            {"username": session["user"]})
        return render_template("pages/profile.html", 
        user=user_profile)
    return redirect(url_for("login"))


@APP.route("/edit/profile/<user_profile_id>", methods=["GET", "POST"])
def edit_profile(user_profile_id):
    """
    Function allowing the session user to edit their 
    profile. It pushes new user details to the DB. 
    It also renders profile template using 
    edit_profile for its main content.
    """
    if request.method == "POST":
        submit = {"$set": {
            "username": request.form.get("username"), 
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password"))
            }
        }
        users.update_one({"_id": ObjectId(user_profile_id)}, submit)
        session["user"] = request.form.get("username")
        flash("User Profile Successfully Updated!")
        return redirect(url_for("profile"))
        
    user_profile = users.find_one({"_id": ObjectId(user_profile_id)})
    return render_template("pages/profile.html", main_content="edit_profile", user=user_profile)


@APP.errorhandler(404)
def page_not_found(error):
    """ 
    Function to render 404 error page
    """
    error = str(error)
    return render_template('pages/404.html', 
    error=error), 404


if __name__ == "__main__":
    APP.run(host=os.environ.get("IP"), 
            port=int(os.environ.get("PORT")), 
            debug=os.environ.get("DEBUG"))
