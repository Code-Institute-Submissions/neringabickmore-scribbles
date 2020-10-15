import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask (__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)

@app.route("/")
@app.route("/about")
def about():
    return render_template("pages/about.html")


@app.route("/account", methods=["GET", "POST"])
def account():
    if session["user"]:
        # grab the session user's credentials from database
        user_profile = mongo.db.users.find_one({"username": session["user"]})
        return render_template("pages/account.html", user=user_profile)
    return redirect(url_for("login"))


@app.route("/edit_profile/<user_profile_id>", methods=["GET", "POST"])
def edit_profile(user_profile_id):
    if request.method == "POST":
        submit = {"$set": {
            "username": request.form.get("username"), 
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password"))
            }
        }
        mongo.db.users.update_one({"_id": ObjectId(user_profile_id)}, submit)
        #update user session to push new username before re-directing
        session["user"] = request.form.get("username")
        flash("User Profile Successfully Updated!")
        return redirect(url_for("account"))
        
    user_profile = mongo.db.users.find_one({"_id": ObjectId(user_profile_id)})
    return render_template("components/forms/edit_profile.html", user=user_profile)


@app.route("/favorites")
def favorites():
    if session["user"]:
        # grab the session user's credentials from database
        user_profile = mongo.db.users.find_one({"username": session["user"]})
        return render_template("pages/favorites.html", user=user_profile)
    return redirect(url_for("login"))


@app.route("/my_reviews")
def my_reviews():
    if session["user"]:
        user_profile = mongo.db.users.find_one({"username": session["user"]})
        reviews = list(mongo.db.reviews.find())
        return render_template("pages/my-reviews.html", user=user_profile, reviews=reviews)
    return redirect(url_for("login"))


@app.route("/add_review", methods={"GET", "POST"})
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
            "emoji": request.form.get("emoji"),
            "rating": request.form.get("rating"),
            "link_to_image": request.form.get("link_to_image"),
            "link_to_buy": request.form.get("link_to_buy"),
            "reviewed_by": session["user"]
        }
        mongo.db.reviews.insert_one(review)
        flash("review added")
        return redirect(url_for("my_reviews"))

    genre = mongo.db.genre.find().sort("genre_category", 1)
    return render_template("components/forms/add-review.html", genre=genre)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
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
            "emoji": request.form.get("emoji"),
            "rating": request.form.get("rating"),
            "link_to_image": request.form.get("link_to_image"),
            "link_to_buy": request.form.get("link_to_buy")
            }
        }
        mongo.db.reviews.update_one({"_id": ObjectId(review_id)}, submit)
        flash("Review Updated!")
        return redirect(url_for("my_reviews"))
        
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    genre = mongo.db.genre.find().sort("genre_category", 1)
    return render_template("components/forms/edit-review.html", review=review, genre=genre)



@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Review Deleted")
    return redirect(url_for("my_reviews"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in database
        existing_user = mongo.db.users.find_one(
            { "username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        
        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        return redirect(url_for("discover", username=session["user"]))

    return render_template("components/forms/register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user: 
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
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

    return render_template("components/forms/login.html")


@app.route("/logout")
def logout():
    # remove user from session cookies
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/discover", methods=["GET", "POST"])
def discover():
    reviews = list(mongo.db.reviews.find())
    return render_template("pages/discover.html", reviews=reviews)
         

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), 
            port=int(os.environ.get("PORT")), 
            debug=True)