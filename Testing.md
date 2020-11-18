# Scribbles - Testing Details #

![Scribbles](/static/images/logo.jpg)

Main [README.md](README.md) file.

View [website](https://scribbles-app.herokuapp.com/) deployed to Heroku.

---

## Contents ##

- [Scribbles - Testing Details](#scribbles---testing-details)
  - [Contents](#contents)
  - [Automated Testing](#automated-testing)
    - [Validation Services](#validation-services)
    - [Client Stories Testing](#client-stories-testing)
      - [**Site Visitor**](#site-visitor)
      - [**Registered Site User**](#registered-site-user)
  - [Manual Testing](#manual-testing)
    - [Testing](#testing)
    - [Additional User Requirements and Expectations testing](#additional-user-requirements-and-expectations-testing)
  - [Bugs discovered](#bugs-discovered)
    - [Solved bugs](#solved-bugs)

---

## Automated Testing ##

### Validation Services ###

- CSS file passed [W3C CSS Validation Services](https://jigsaw.w3.org/css-validator/validator) without faults.
- Vendor prefixes added using [Autoprefixer](https://autoprefixer.github.io/).
- Json files in data schemas folder were validated with [JsonLint](https://jsonlint.com/) and all passed.
- Script.js file was missing a few semicolons but otherwise passed [jshint.com](https://jshint.com/) validation without issues.
- All HTML files were tested using [W3 validator](https://validator.w3.org) to identify any error or warnings. The validator did throw quite a few errors. The ones that could be fixed (related directly to html elements), however in the instances where python was used I was unable to correct such errors for obvious reasons - I need data to be pushed from he database to the app.

### Client Stories Testing ###

The following section goes through each of the user stories from the UX section of [README.md](\scribbles\README.md).

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

- **Responsive design**

The app has a different layout options, focused on *mobile-first* design in mind as more users are expected to use mobile rather than larger devices, such as a tablet or a laptop/desktop.
![mobile and desktop display](/wireframes/testing-images/responsive-design.jpg)

### Testing ###

- **Sliding banner** on a home/about page

![sliding banner images](/wireframes/testing-video/sliding-banner.gif)
  
- **Register** account form
  
  The user is able to create a brand new account. The app will test if the user already exists based on the username and if it doesn't it allow the registration.

![register](/wireframes/testing-video/register.gif)

- **Sign in/out** functionality

    The user is able to login and logout from their account. If the user enters incorrect credentials when logging in they are notified to check the details.

![login](/wireframes/testing-video/login.gif)
![logout](/wireframes/testing-video/logout.gif)

- **Favorites** functionality

    The user is able to add reviews from discover page (including their own) to the favorites page.

![favorites](/wireframes/testing-video/add-to-favorites.gif)

- **Easy navigation** to external sites

   The user is redirected to a website when clicks on *purchase* a book button.

![purchase the book](/wireframes/testing-video/redirecto-to-vendor.gif)

- **Search function**

    The user is able to search books by *title*, *author*, *genre* or any other word that is on the review.

![search functionality](/wireframes/testing-video/search.gif)

### Additional User Requirements and Expectations testing ###

- **Visually pleasant app design**
  
  The feedback I was given from my colleagues, friends and family as well as fellow students is that the app has a pleasant design.

- **Easy site navigation**

The users are offered a self-explanatory site navigation by using text where required or else easy to understand icons.

- **Information of the content layed out in a simple and clear way on both mobile and larger screens**

The information is indeed layered in the most simplistic way possible. The feedback I received from colleagues, fellow students and family is that they find it super easy to navigate through the website.

- **Self-explanatory icons where text is absent**

I have asked my 5 year old son to explain to me what the icons mean. It was very clear to him what the icons were and was able to easily explain them. Based on this, I am comfortable to say that the icon are self-explanatory.

- **User information is protected by the site**
  
User information obtained through the site is not shared with third parties. Also, the user password is hashed when stored in the database.

- **User is able to manipulate elements of the particular page**

The user can click buttons on the page, enter information where the forms are provided or select elements supplied on the forms.

- **Quick app load time**

Images used on the app were optimized to allow quick loading time.

## Bugs discovered ##

### Solved bugs ###

1: @app route wasn't pushing new username to the template.

**Bug-fix:** insert new bit of code to update the username details before rendering the template.
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

2: All users in their my-reviews.html are able to see other users entries. This shouldn't happen and they should only see their own entries in this template. The code was:

```python
@app.route("/my_reviews")
def my_reviews():
    if session["user"]:
        user_profile = mongo.db.users.find_one({"username": session["user"]})
        reviews = list(mongo.db.reviews.find())
        return render_template("pages/my-reviews.html", user=user_profile, reviews=reviews)
    return redirect(url_for("login"))

```

**Bug-fix:** changed the reviews  

```python
reviews = list(mongo.db.reviews.find({"reviewed_by": session["user"]}))

```

3: Discover.html shows "favorite" button to both registered and non-registered users.

**Bug-fix:** add below to the button:

```python
{% if session.user %}
    <button class="btn btn-primary">Favorite</button>
{% endif %}

```

4: Favorites button in discover.html adds the same review to favorites multiple times.

The original code:

```python
@app.route("/add/favorites/<review_id>")
def add_favorites(review_id):
    if session["user"]:
        current_user = {'username': session['user'].lower()}
        favorite_reviews = users.find_one(current_user)["favorites"]
        if ObjectId(review_id) in favorite_reviews:
    return redirect(url_for('discover'))
```

**Bug-fix:** check if the favorite item already exists first before proceeding:

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

5: On registration, the user is not shown a flash message greeting them.

![registration without flash message](/wireframes/testing-video/register-with-bug.gif)

**Bug-fix:** Add flash message code

```python
flash("Welcome, {}".format(
                        request.form.get("username")))
        return redirect(url_for("discover", username=session["user"]))
```

6: If a user deletes one of their reviews, which is *favorited* by one other users, their favorites template may show error as that review in the collection no longer exists.

**Bug-fix:** Add below code to ```delete_review``` function, which deletes ObjectId's from all users' favorites arrays if the review owner deletes the review from reviews collection.

```python
users.update_many(
        {},
        {"$pull": {"favorites": ObjectId(review_id)}}
    )
```

7: If the user didn't added any reviews to their **favorites**, they don't have a message on their **favorites** page suggesting they should add some reviews to have anything displayed on the page.

**Bug-fix:** Add below code to the *favorites.html* template before the ```{% endfor %}```:

```html
 {% else %}
        <div class="col-12">
            <p class="text-center my-4"> you currently have no reviews in your favorites. </p>
            <p class="text-center my-4"> why don't you try to add some? </p>
        </div>
```

8: If the user didn't add any of their own reviews to the app, **my reviews** page doesn't have a message to encourage the user to doing so.

**Bug-fix:** Add below code to the *my-reviews.html* template before the ```{% endfor %}```:

```html
 {% else %}
        <div class="col-12">
            <p class="text-center my-4"> you currently have no reviews. </p>
            <p class="text-center my-4"> why don't you try to add some? </p>
        </div>
```

9: If the review owner deletes the review, which is favorited by other users, then those users' favorites template shows error. 

**Bug-fix:** Add additional code to delete review_id from favorites if the owner of the review chooses to delete their entry.

```python
 users.update_many(
        {},
        {"$pull": {"favorites": ObjectId(review_id)}}
    )
```

10: When the user edits their review, previously selected genre category wasn't displaying and by default ```Action & Adventure``` were being pushed by default.

Original code:

```html
<!-- Select Genre -->
            <div class="form-group mb-0">
                <label for="genre_category">genre</label>
                <select name="genre_category" class="form-control" id="genre_category">
                    {% for genre in genre %}
                    <option value="{{ genre.genre_category }}">{{ genre.genre_category }}</option>

                    {% endfor %}
                </select>
            </div>

```

**Bug-fix:** inserted extra line of code to fix it.

```html
<!-- Select Genre -->
            <div class="form-group mb-0">
                <label for="genre_category">genre</label>
                <select name="genre_category" class="form-control" id="genre_category">
                    <option value="{{ review.genre }}" selected>{{ review.genre }}</option>
                    {% for genre in genre %}
                    <option value="{{ genre.genre_category }}">{{ genre.genre_category }}</option>

                    {% endfor %}
                </select>
            </div>
```

11: Modal on *delete button* in my-reviews.html was looping through all of the items in the collection and therefore deleting the first item in the collection instead of the one user selected.

**Bug-fix:** inserted {{ loop.index }} to modal ID:

```html
<!-- Remove from favorites button
                    which triggers modal
                -->
                <a class="btn align-self-center" data-toggle="modal" data-target="#deleteFavoriteModal{{ loop.index }}"><i
                        class="far fa-trash-alt icon-btn"></i></a>

                <!-- Modal -->
                <div class="modal fade" id="deleteFavoriteModal{{ loop.index }}" tabindex="-1"
                    aria-labelledby="deleteFavoriteModalLabel" aria-hidden="true">
                </div>
```
