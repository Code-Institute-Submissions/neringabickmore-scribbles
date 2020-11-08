# Scribbles - Testing Details #

---

## Contents ##

---

## Automated Testing ##

### Validation Services ###

### Client Stories Testing ###

The following section goes through each of the user stories from the UX section of [README.md](\scribbles\README.md)

#### **Site Visitor** ####

1. As a **user** I want to be able to find out the information **about** the app.
    - The User is able to view information about the app clicking on **about** navigation on the navbar, which takes them there. Also, About page is the first to render then the app is loaded.
2. As a **user** I want ot be able to **discover** some book review samples.
   - The user is able to discover book review samples by following **discover** navigation on the navbar which displays all existing book reviews, including those of the user themselves if they have made any entries.
3. As a **user** I want to be able to **login** to my account.
   - Following **login** button on the navbar, the user is able to login to their account.
4. As a **user** I want to **register** if I don't have an account.
   - Following **register** button on the navbar, the user is able to create a new account. The form will prompt the user if there is a duplication based on the username.
![register video](/wireframes/testing-video/register.gif)
![existing user](/wireframes/testing-video/existing-user.gif)

5. As a **user** I want to find **contact details** for the site admin.
    - As this feature was proposed for future development features, unfortunately the users will not be able to find the contact details of the site admin. Instead, they could potentially contact the owner of the app owner via social media at present.
6. As a **user** I want to find **social media** accounts connected to the site.
   - All users are able to find **social media** icons in the footer of the page.

![header image](/wireframes/testing-images/header.jpg)
![discover image](/wireframes/testing-images/discover.jpg)
![login image](/wireframes/testing-images/login.jpg)
![footer image](/wireframes/testing-images/footer.jpg)

#### **Registered Site User** ####

1. As a **user** I want to be able to **Login** to my account.
   - When a user has an existing account, they can follow **login** navigation on the navbar, enter their credentials and click login to view their account. As you see in the below demonstration, the user also sees a greeting once logged in and is directed to **discover** page of the app.

   ![login test video](/wireframes/testing-video/login.gif)

2. As a **user** I want to be able to  **logout** of my account.
   - The user is able to logout of their account by navigating to **account** on the navbar and choosing the option to logout.
  
    ![logout](/wireframes/testing-video/logout.gif)

3. As a **user** I want to be able to **edit my account** information.
   - The user is able to edit their account by navigating to **account** on the navbar and choosing the option to **view profile** and then **edit** button. If they choose **cancel** button, the user is taken to **discover reviews** page.
  
   ![edit account](/wireframes/testing-video/edit-account.gif)

4. As a **user** I want to be able to **view** other users' book reviews.
   -The user has a few options how to **view** other users reviews:
   1. When they login, they are directed to **discover** page
   2. When they navigate to **discover** button on navbar
   3. When they *cancel* **edit account** option

   ![heart reviews](/wireframes/testing-video/discover.gif)

5. As a **user** I want to be able to *heart* other users' book **reviews**.
   - All registered users are able to *heart* other users' reviews by clicking on the *heart* button on **discovery** page. They get a notification on the screen once they add a review to their **favorites**.
  
    ![favorites page](/wireframes/testing-video/add-to-favorites.gif)
  
6. As a **user** I want to be able to **access** *hearted* books on a **favorites** page.
   -The user is able to view **hearted** reviews if they navigate to navbar and click on **favorites** button. Please note, if the user didn't **heart** any reviews, they will not have content on display on their **favorites** page.Please refer to the video above.

7. As a **user** I want to be able to **remove** other user's book reviews from my **favorites**.
   - The user has an option to remove **hearted** reviews from their **favorites** page by clicking on **bin** button.
  
   ![remove favorite](/wireframes/testing-video/remove-from-favorites.gif)

8. As a **user** I want to be able to **access my book reviews** I have created before.
   - When the user navigates to navbar and clicks on **my reviews** button, they are re-directed to the **my reviews** page. Please note, if the user hasn't submitted any reviews they will not have content on display except for **add review** button.
  
    ![my reviews](/wireframes/testing-video/my-reviews.gif)

9. As a **user** I want to be able to **create new** book reviews.
    - The user can add new reviews by clicking on **add review** button at the top of the **my reviews** page.

    ![add review](/wireframes/testing-video/add-review.gif)

10. As a **user** I want to be able to **edit existing** book reviews.
    - The user is able to edit one of their reviews by clicking on **edit** button at the top of each review. They are then redirected to **edit review template**. The template will display the current review details that are pulled from the database and they can therefore change only the parts they wish to change. At this stage, the user has an option to **update** the review or **cancel** the action. Regardless of the option the user choose, they are re-directed back to **my reviews** page.
  
    ![edit review](/wireframes/testing-video/update-review.gif)

11. As a **user** I want to be able to **delete** my book reviews.
    - The user is able to **delete** one of their own reviews by clicking on the **bin** button at the top of each review.

    ![remove review](/wireframes/testing-video/delete-review.gif)

---

## Manual Testing ##

### Testing undertaken on Mobile ###

### Testing undertaken on tablet and desktop ###

### Bugs discovered ###

#### Solved bugs ####

1. @app route wasn't pushing new username to the template; The bug was fixed by inserting new bit of code to update the username details before rendering the template.
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

4. Favorites button in discover.html adds the same review to favorites multiple times.
   Original code:

```python
@app.route("/add/favorites/<review_id>")
def add_favorites(review_id):
    if session["user"]:
        user_profile = users.find_one({'username': session['user'].lower()})
        users.update(user_profile, {"$push": {"favorites": ObjectId(review_id)}})
        flash("Review added to favorites")
        return redirect(url_for('discover'))
    return redirect(url_for('discover'))
```

Bug-fix: check if the favorite item already exists first before proceeding:

```python
if session["user"]:
        # check if favorite review already exists in database
        favorite_review_exists = mongo.db.favorites.find_one({"favorite": review_id})

        # if the favorite review already in the database - it flashes a message
        favorite_review_exists = users.find_one({"favorites": ObjectId(review_id)})
        if favorite_review_exists:
            flash("This review is already in your favorites")
            return redirect(url_for("discover"))
```

5. On registration, the user is not shown a flash message greeting them.

![registration without flash message](/wireframes/testing-video/register-with-bug.gif)

Bugfix: Add flash message code

```python
flash("Welcome, {}".format(
                        request.form.get("username")))
        return redirect(url_for("discover", username=session["user"]))
```

### Unsolved bugs ###

1. If the user didn't added any reviews to their **favorites**, they don't have a message on their **favorites** page suggesting they should add some reviews to have anything displayed on the page.
2. If the user didn't add any of their own reviews to the app, **my reviews** page doesn't have a message to encourage the user to doing so.