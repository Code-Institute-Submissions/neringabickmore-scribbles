# Scribbles - Testing Details #

---

## Contents ##

---

## Automated Testing ##

### Validation Services ###

### Client Stories Testing ###

---

## Manual Testing ##

### Testing undertaken on Mobile ###

### Testing undertaken on tablet and desktop ###

### Bugs discovered ###

#### Solved bugs ####

   1. @app route wasn't pushing new username to the template; The bug was fixed by inserting new bit of code to update the username details before rendering the templae.
Also, the same @app.route wasn't generating new password and also needed to looked into:

```python

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
```

2. All users in their my-reviews.html are able to see other users entries. This shouldn't happen and they should only see their own entries in this template. The code was:

```python
@app.route("/my_reviews")
def my_reviews():
    if session["user"]:
        user_profile = mongo.db.users.find_one({"username": session["user"]})
        reviews = list(mongo.db.reviews.find())
        return render_template("pages/my-reviews.html", user=user_profile, reviews=reviews)
    return redirect(url_for("login"))

```

Bug-fix: changed the reviews  

```python
reviews = list(mongo.db.reviews.find({"reviewed_by": session["user"]}))

```

3. Discover.html shows "favorite" button to both registered and non-registered users.
   Bug-fix by adding below to the button:

```python
{% if session.user %}
    <button class="btn btn-primary">Favorite</button>
{% endif %}

```

### Unsolved bugs ###

