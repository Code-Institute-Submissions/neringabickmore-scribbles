# Scribbles #

![Scribbles](/static/images/logo.jpg)

[Scribbles](https://scribbles-app.herokuapp.com/) is an interactive book review app where site users create, read, update and delete their own content.

About three years ago I have made a conscious decision to read more books. I have read quite a lot of them since but could never keep the track of them. I am also always interested in recommendations from other like-minded readers. When it come to creating my third milestone project at [Code Institute](https://codeinstitute.net/), it had to be a book review app where I can share my reviews with site visitors and other users.

![Site display on different screens](/wireframes/testing-images/responsive-design.jpg)

---

## Contents ##

- [Scribbles](#scribbles)
  - [Contents](#contents)
  - [UX](#ux)
    - [Project Goals](#project-goals)
    - [Site Owner Goals](#site-owner-goals)
    - [User Stories](#user-stories)
      - [**Site Visitor**](#site-visitor)
      - [**Registered Site User**](#registered-site-user)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
      - [**Requirements**](#requirements)
      - [**Expectations**](#expectations)
    - [Design Choices](#design-choices)
      - [**Fonts**](#fonts)
      - [**Colours**](#colours)
    - [Wireframes](#wireframes)
      - [**Site Map**](#site-map)
      - [**Site Layout**](#site-layout)
      - [**User Account Creation**](#user-account-creation)
      - [**Database design**](#database-design)
      - [**Data Storage Types**](#data-storage-types)
  - [Technologies](#technologies)
    - [Languages](#languages)
    - [Libraries & Tools](#libraries--tools)
  - [Features](#features)
    - [Implemented Features](#implemented-features)
    - [Future Features](#future-features)
  - [Changes applied since planning](#changes-applied-since-planning)
    - [Admin feature](#admin-feature)
    - [Search feature](#search-feature)
    - [Emojis](#emojis)
    - [About template design](#about-template-design)
    - [Register / Login templates](#register--login-templates)
    - [Forms and page templates design](#forms-and-page-templates-design)
    - [Color palette](#color-palette)
    - [Sort review by genre as a heading](#sort-review-by-genre-as-a-heading)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Cloning *Scribbles* from GitHub](#cloning-scribbles-from-github)
    - [Deploying Scribbles to Heroku](#deploying-scribbles-to-heroku)
  - [Credits](#credits)
    - [Images](#images)
    - [Image editing](#image-editing)
    - [Code ideas](#code-ideas)
  - [Acknowledgements](#acknowledgements)

---

## UX ##

### Project Goals ###

The **goals** of this project are:

- Create an **interactive app** where site visitors can **create a user account**
- The app allows the users to manage their content, such as **creating** it, **reading** it **editing** it later or **delete** it completely.
- The app that has different content functionalities for **site visitors** and **users**.
- The app should also be able to store required data, which is available for access when required

### Site Owner Goals ###

- To provide a platform for the users to share their personal views about the books they have read.
- Encourage users to share their recommendations where they should buy the book they have reviewed, ideally independent online book shops.
- Build a community of book readers.
- Monetise the platform through donations to cover platform maintenance costs (potentially in the future).

### User Stories ###

#### **Site Visitor** ####

- As a **user** I want to be able to find out the information **about** the app.
- As a **user** I want ot be able to **discover** some book review samples.
- As a **user** I want to be able to **login** to my account.
- As a **user** I want to **register** if I don't have an account.
- As a **user** I want to find **contact details** for the site admin.
- As a **user** I want to find **social media** accounts connected to the site.

#### **Registered Site User** ####

- As a **user** I want to be able to **Login** to my account.
- As a **user** I want to be able to  **Logout** of my account.
- As a **user** I want to be able to **edit my account** information.
- As a **user** I want to be able to **view** other users' book reviews.
- As a **user** I want to be able to *heart* other users' book **reviews**.
- As a **user** I want to be able to **access** *hearted* books on a **favorites** page.
- As a **user** I want to be able to **remove other user's book reviews from my *favorites***.
- As a **user** I want to be able to **access my book reviews** I have created before.
- As a **user** I want to be able to **create new** book reviews.
- As a **user** I want to be able to **edit existing** book reviews.
- As a **user** I want to be able to **delete** my book reviews.

[Back to content](#contents)

### User Requirements and Expectations ###

#### **Requirements** ####

- Visually pleasant app design
- Easy site navigation
- Information of the content layed out in a simple and clear way on both mobile and larger screens
- Self-explanatory icons where text is absent

#### **Expectations** ####

- User information is protected by the site
- User is able to manipulate elements of the particular page
- Quick app load time

[Back to content](#contents)

### Design Choices ###

The aim of the site design is to ensure the focus is on the book reviews. I have chosen neutral color palette and will adopt minimalistic site features throughout. Icons used on the site are easy to understand and read and therefore text use is avoided where possible.

#### **Fonts** ####

I chose easy to read and light fonts for this app. I am keeping it simple and will only use two of the fonts:

- *Headers, titles*

  ```font-family: 'Rubik', sans-serif;```

- *Paragraphs, descriptions*

  ```font-family: 'Lato', sans-serif;```

#### **Colours** ####

I chose the colours that I felt are quite delicate and not overpowering the main content of the app.

![Colour palette](/wireframes/color-palette/color-palette.jpg)

[Back to content](#contents)

### Wireframes ###

#### **Site Map** ####

Firstly, I have created a site [map](/wireframes/flowcharts/sitemap.png) to identify clear features the site will have when viewed by the visitor, registered user, and admin.

#### **Site Layout** ####

I designed my site moc-ups using [balsamiq wireframes](https://balsamiq.com/). I was focusing on defining the basic layout structure of the app and identifying how displays would change on different screen sizes such as [mobile and larger screens](/wireframes/site-wireframes/about.visitor.png).

You can view all wireframes created for this project [here](/wireframes/site-wireframes).

#### **User Account Creation** ####

To make user account creation logic easier to understand and simplify the management of it, I have created [workflow-chart](/wireframes/flowcharts/account-creation.jpg).

#### **Database design** ####

Utilising the NoSQL features that MongoDB provides, I was able to map out the following collections:

[Review Collection](/wireframes/data-schemas/review-collection.json)
  
**Title**|**Key in Collection**|**Data Type**
:-----:|:-----:|:-----:
Book Id|_id|ObjectId()
Title|title|string
Author|author|string
Genre|genre|ObjectId()
Length|length|string
Ease of Reading|ease-of-reading|string
Plot Summary|plot-summary|string
Favorite Quote|favorite-quote|string
Book rating|rating|string
Image|link-to-image|string
Buy a Book|link-to-buy|string

[Genre Collection](wireframes/data-schemas/genre.json)

**Title**|**Key in Collection**|**Data Type**
:-----:|:-----:|:-----:
Genre ID|_id|ObjectId()
Title|title|string

[User Collection](/wireframes/data-schemas/user-collections.json)

**Title**|**Key in Collection**|**Data Type**
:-----:|:-----:|:-----:
User ID|_id|ObjectID()
Username|username|string
Email Address|email|string
Favorite Books|favorites|[ObjectId()]

#### **Data Storage Types** ####

The types of data that are store in the MongoDB database:

- ObjectID
- String
- Boolean
- Object
- Array
- Binary

[Back to content](#contents)

---  

## Technologies ##

### Languages ###

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python](https://www.python.org/)

### Libraries & Tools ###

- [jQuery](https://jquery.com/)
- [Popper](https://popper.js.org/)
- [Popper JS](https://popper.js.org/)
- [Bootstrap](https://getbootstrap.com/)
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
- [PyMongo](https://pypi.org/project/pymongo/)
- [Flask](https://www.fullstackpython.com/flask.html)
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
- [Font-Awesome](https://fontawesome.com/icons?d=gallery)
- [Google fonts](https://fonts.google.com/)
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)
- [Heroku](https://www.heroku.com/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Color editor](https://coolors.co/)
- [Image editor](https://www.birme.net/)

[Back to content](#contents)

---

## Features ##

### Implemented Features ###

- **Responsive design**

The app has a different layout options, focused on *mobile-first* design in mind as more users are expected to use mobile rather than larger devices, such as a tablet or a laptop/desktop.

- **Sliding banner** on a home/about page
  
- **Register** account form

- **Sign in/out** functionality

- **Favorites** functionality

- **Easy navigation** to external sites

The user is redirected to a website when clicks on *purchase* a book button.

- **Search function**

The user is able to search books by entering any text that may appear on the book review (i.e. author, title, length, genre etc).

### Future Features ###

- **Language Selector**
  
The user is able to choose English or Lithuanian language to view the site.

- **Site admin** edit

Site admin feature allows deletion of inappropriate reviews, change of book review form items, as well as deletion of the registered user accounts.
  
- **Defence mechanism**
  
The user gets a notification before *delete* action is activated in app commands.

- **Password re-set**

[Back to content](#contents)

---

## Changes applied since planning ##

### Admin feature ###

- I have decided to move one key feature of the project to future features which is admin side of it. This is due to the fact that the project has taken longer to complete than originally anticipated and the time constrains I have.

### Search feature ###

- During the planning stage of the project it seemed like a good idea to have search option in discover, favorites, and my reviews templates. During the process of developing this project further I came to realization that the users may not have an extensive amount of personal reviews or favorites reviews at the beginning that they would require such feature. Should the app users grow and the list of reviews increase I will consider implementing this feature in the other two templates and therefore I only have this feature in discover template.

### Emojis ###

- My initial idea was to have the users to sum up their views on the book in 3 emojis. I have talked to friends and family and the feedback I was given that quite a few of them disliked emojis completely and it would put them off using the app. To target wider audience I have decided to remove emojis completely.

### About template design ###

- I have decided to remove any reviews from About template due to the fact that I already have a sole page dedicated to display all of the templates. To me the About page look neater without any reviews listed on it. I was also contemplating should I incorporate about page with the discover page, however given the fact that registered users are not seeing about page after logging in at all by default, I have decided against it. In my opinion the design of the page looks neater and more appealing this way.

### Register / Login templates ###

- I have made slight amendment to initial design of both register and login pages by giving the user an option to switch to Login if they already are registered and just click the wrong button and visa versa. In my opinion this way I am enhancing user experience and they can switch from login to register pages with ease.

### Forms and page templates design ###

- The wireframes I have created indicated initial idea of the content the templates and forms should have. During the creation of the app I have assessed carefully how the layout of each form should look like to create the most appealing and pleasant design for the user. I have applied the same tactic when choosing the layout of the page templates. As a result, the final version of the app is likely to have different shape buttons, icons and their positioning on the templates in comparison to the wireframes.

### Color palette ###

- The color palette you see in the final version of the wireframe differ to the original one very slightly. During the development stage of the project the feedback I was given is that some colors blend too much and to enhance visual user experience I needed to reconsider bringing in some base colours of black and white as well as losing one of the shades.

### Sort review by genre as a heading ###

- My initial idea was to render html templates (discover, my reviews, and favorites) with the genre header element. I have decided against it during development stage of the project as in my opinion it's nice to have a genre header per each review instead.
  
---

## Testing ##

Testing information can be found in a separate [Testing.md](Testing.md) file.

[Back to content](#contents)

---

## Deployment ##

*Scribbles* was developed using Visual Studio Code, using Git and GitHub to host the repository.

### Cloning *Scribbles* from GitHub ###

**Ensure** you have the following installed:

- [PIP](https://pypi.org/project/pip/)
- [Python 3](https://www.python.org/)
- [Git](https://git-scm.com/)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

**Make sure you have an account at [MongoDB](https://www.mongodb.com/) in order to construct the database.**

*WARNING: You may need to follow a different guide based on the OS you are using. For more information, read up [here](https://python.readthedocs.io/en/latest/library/venv.html)*

1: **Clone** the *Scribbles* repository by either downloading from [source](https://github.com/neringabickmore/scribbles), or if you have Git installed typing the following command into your terminal:

```bash
git clone https://github.com/neringabickmore/scribbles
```

2: **Navigate** to this folder in your terminal window and **install** required modules to run the application using the following command:

```bash
python -m pip -r requirements.txt
```

3: **Initialize** virtual environment by typing the following command into the terminal:

```bash
py -m venv virtual
```

4: If you're using bash and the command doesn't run, you may also need to set user policy to *un-restricted* by typing the following command in your terminal:

```bash
Set-ExecutionPolicy -Scope CurrentUser
```

then:

```bash
unrestricted
```

5: In MongoDB, create a new database called *scribbles* with four collections: *users*, *reviews*, *genre*, and *emoji*.

6: Back in your VS Code, create a file to hold your environment variables and call it *env.py*. Make sure you add file to your *.gitignore* file before committing.

If you do end up committing by mistake, you can correct this by typing the following command:

```bash
git rm -r --cached env.py
echo env.py >> .gitignore
```

5: Your env.py file should contain the following:

```bash
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "YOUR_SECRET_KEY")
os.environ.setdefault("MONGO_URI", "YOUR_MONGODB_URI")
os.environ.setdefault("MONGO_DBNAME", "YOUR_DATABASE_NAME")
```

*Please make sure you update your **SECRET_KEY**, **password**, **database_name**, and **DATABASE_NAME***

7: You can now run your application locally by typing the following command in your terminal:

```bash
python run.py
```

*You may need to change local host in browser to 127.0.0.1:5000*

### Deploying Scribbles to Heroku ###

1: **Login** to Heroku and create a new app.

2: **Create** a requirements.txt file using the following command:

```bash
pip3 freeze --local > requirements.txt
```

3: **Create** a Procfile with the following command:

```bash
echo web: python run.py > Procfile
```

4: **Push** these newly created files to your repository master.

5: **Add heroku remote** to your git repository by getting the heroku git URL from the heroku account settings. Then type the following: 

```bash
git remote add heroku https://git.heroku.com/your-heroku-repo
```

6: Push *scribbles* to your heroku:

```bash
git push heroku master
```

7: In your heroku app, **set** the following variables:

**Key**|**Value**
:-----:|:-----:
HOSTNAME|0.0.0.0
PORT|5000
MONGO_URI|YOUR_MONGODB_URI
SECRET_KEY|YOUR_SECRET_KEY

  ** Please make sure you enter your own *SECRET_KEY*, and *MONGO_URL*.

8: Click the deploy button on the Heroku dashboard.
9: The site has been deployed the Heroku.

[Back to content](#contents)

---

## Credits ##

### Images ###

### Image editing ###

- I have used the snippet tool for capturing screengrabs which I saved as images.
- MS Paint 3D to edit images as required.
- A handy [Birme](https://www.birme.net/?target_width=300&target_height=300&quality=100&border_width=1&border_color=%23bd3d3a) site allowed me to resize the images all at once.
- I have also used [giphy.com](https://giphy.com/) to convert MP4 video files to gif files used in Testing.md.

### Code ideas ###

- To enable better understanding on how to plan database design, I have [referred to](https://github.com/Geomint/beer-time) the fellow student project.
- Scroll Up Button borrowed from [W3Schools](https://www.w3schools.com/howto/howto_js_scroll_to_top.asp) tutorial.
- Redirection to vendor site to purchase the books idea borrowed from [here](https://github.com/Pysched/MS3-DM).

[Back to content](#contents)

---

## Acknowledgements ##

I would like to recognize the people who have helped me through this project:

- My mentor [Simen Daehlin](https://github.com/Eventyret) for his time, patience, and support in helping me to adopt the best coding practices and believing in me! Thank you!
- Code Institute tutors [Tim](https://github.com/TravelTimN) for amazing Python tutorials, [Igor](https://github.com/bravoalpha79), and [Miklos](https://github.com/Sarosim) who have helped me with technical struggles and made me think outside the box to solve my python problems.

- My fellow Code Institute slack community, especially [Simon Castagna](https://github.com/jumboduck) for listening to my struggles and pushing me forward.

- My husband, family, and friends for continuously testing my project and not giving up on me 😊

**Thank you all for pushing me forward!**

[Back to content](#contents)
