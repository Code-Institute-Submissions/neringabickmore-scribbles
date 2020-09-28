# Scribbles #

[Scribbles]() is an interactive book review app where site users create, read, update and delete their own content.

About three years ago I have made a conscious decision to read more books. I have read quite a lot of them since but could never keep the track of them. I am also always interested in recommendations from other like-minded readers. When it come to creating my third milestone project at [Code Institute](https://codeinstitute.net/), it had to be a book review app where I can share my reviews with site visitors and other users.

![Site display on different screens](/wireframes/)

---

## Contents ##

- [Scribbles](#scribbles)
  - [Contents](#contents)
  - [UX](#ux)
    - [Project Goals](#project-goals)
    - [Site Owner Goals](#site-owner-goals)
    - [User Stories](#user-stories)
      - [**Site Visitor**](#site-visitor)
      - [**Site Admin**](#site-admin)
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
- The app that has different content functionalities for **site visitors**, **users** and **admin**
- The app should also be able to store required data, which is available for access when required

### Site Owner Goals ###

- To provide a platform for the users to share their personal views about the books they have read.
- Encourage users to share their recommendations where they should buy the book they have reviewed, ideally independent online book shops.
- Build a community of book readers.
- Monetise the platform through donations to cover platform maintenance costs.

### User Stories ###

#### **Site Visitor** ####

- As a **site visitor** I want to be able to find out the information **about** the app.
- As a **site visitor** I want ot be able to **discover** some book review samples.
- As a **site visitor** I want to be able to **login** to my account.
- As a **site visitor** I want to **register** if I don't have an account.
- As a **site visitor** I want to find **contact details** for the site admin.
- As a **site visitor** I want to find **social media** accounts connected to the site.

#### **Site Admin** ####

- As a **site admin** I want to be able to **access** needed **information** about **registered** site **users**.
- As a **site admin** I want to be able to **delete** registered users.
- As a **site admin** I want to be able to **discover and access** all of the book reviews on the site.
- As a **site admin** I want to be able to **delete** book reviews.
- As a **site admin** I want to be able to **edit** book review template.
  
#### **Registered Site User** ####

- As a **site user** I want to be able to **Login** to my account.
- As a **site user** I want to be able to  **Logout** of my account.
- As a **site user** I want to be able to **edit my account** information.
- As a **site user** I want to be able to **view other users' book reviews**.
- As a **site user** I want to be able to ***heart* other users' book reviews**.
- As a **site user** I want to be able to **access** all of the **other users' book reviews** I have *hearted* on a **separate page** such as **favorites**.
- As a **site user** I want to be able to **remove other user's book reviews from my *favorites***.
- As a **site user** I want to be able to **access my book reviews** I have created before.
- As a **site user** I want to be able to **create new** book reviews.
- As a **site user** I want to be able to **edit existing** book reviews.
- As a **site user** I want to be able to **delete** my book reviews.

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
- Users are able to find and contact admin when required (i.e. account deletion)

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

![Colour palette](/wireframes/colour_palette/color_palette.jpg)

[Back to content](#contents)

### Wireframes ###

#### **Site Map** ####

Firstly, I have created a site [map](/wireframes/flowcharts/sitemap.png) to identify clear features the site will have when viewed by the visitor, registered user, and admin.

#### **Site Layout** ####

I designed my site moc-ups using [balsamiq wireframes](https://balsamiq.com/). I was focusing on defining the basic layout structure of the app and identifying how displays would change on different screen sizes such as [mobile and larger screens](/wireframes/site_wireframes/about.visitor.png).

You can view all wireframes created for this project [here](/wireframes/site_wireframes).

#### **User Account Creation** ####

To make user account creation logic easier to understand and simplify the management of it, I have created [workflow-chart](/wireframes/flowcharts/account_creation.jpg).

#### **Database design** ####

Utilising the NoSQL features that MongoDB provides, I was able to map out the following collections:

[Review Collection](/wireframes/data_schemas/review_collection.json)
  
**Title**|**Key in Collection**|**Data Type**
:-----:|:-----:|:-----:
Book Id|_id|ObjectId()
Title|title|string
Author|author|string
Genre|genre|array
Length|length|string
Ease of Reading|ease_of_reading|string
Plot Summary|plot_summary|string
Favorite Quote|favorite_quote|string
Emoji|emoji|array
Book rating|rating|string
Image|link_to_image|string
Buy a Book|link_to_buy|string

[User Collection](/wireframes/data_schemas/user_collections.json)

**Title**|**Key in Collection**|**Data Type**
:-----:|:-----:|:-----:
User ID|_id|ObjectID()
Username|username|string
Email Address|email|string
Favorite Books|favorites|ObjectId()

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

![site views on different displays]()

- **Sliding banner** on a home/about page
  
- **Register** account form

- **Sign in/out** functionality

- **Favorites** functionality

- **Easy navigation** to external sites

The user is redirected to a website when clicks on *purchase* a book button.

- **Search function**

The user is able to search books by *title*, *author*, and *genre*.

- **Site admin** edit

Site admin feature allows deletion of inappropriate reviews, change of book review form items, as well as deletion of the registered user accounts.

### Future Features ###

- **Language Selector**
  
The user is able to choose English or Lithuanian language to view the site.
  
- **Defence mechanism**
  
The user gets a notification before *delete* action is activated in app commands.

- **Password re-set**

[Back to content](#contents)

---

## Testing ##

Testing information can be found in a separate [Testing.md](Testing.md) file.

[Back to content](#contents)

---

## Deployment ##

*Scribbles* was developed using Visual Studio Code, using Git and GitHub to host the repository.

### Cloning *Scribbles* from GitHub ###

**Ensure** you have the following installed:

- PIP
- Python 3
- Git

**Make sure you have an account at [MongoDB](https://www.mongodb.com/) in order to construct the database.**

*WARNING: You may need to follow a different guide based on the OS you are using. For more information, read up [here](https://python.readthedocs.io/en/latest/library/venv.html)*

1: **Clone** the *Scribbles* repository by either downloading from [source](https://github.com/neringabickmore/scribbles), or if you have Git installed typing the following command into your terminal.

```bash
git clone https://github.com/neringabickmore/scribbles
```

2: **Navigate** to this folder in your terminal.
3: **Enter** the following command into your terminal.

```bash
python3 -m .venv venv
```

4: **Initilaize** the environment by using the following command.

```bash
.venv\bin\activate
```

5: **Install** the relevant requirements & dependancies from the requirements.txt file.

```bash
pip3 -r requirements.txt
```

6: In your IDE now **create** a file where you can store your SECRET_KEY and your MONGO_URI, follow the schema structure located in data/schemas to properly setup the Mongo Collections.

*NOTE: I developed this website on Visual Studio Code and used the following settings.json file, delete and replace with your values.*

```json
{
    "python.pythonPath": "env/bin/python",
    "python.terminal.activateEnvironment": true,
    "python.linting.enabled": true,
    "python.linting.pylintArgs": ["--load-plugins=pylint_flask"],
    "files.autoSave": "onFocusChange",
    "files.useExperimentalFileWatcher": true,
    "terminal.integrated.env.osx": {
      "SECRET_KEY": "<your_secret_key>",
      "DEV": "1",
      "FLASK_DEBUG": "1",
      "MONGO_URI": "<your_mongo_uri>"
    }
}
```

7: Run the application using

```bash
flask run
```

or

```bash
Python3 run.py
```

### Deploying Scribbles to Heroku ###

1: **Create** a requirements.txt file using the following command.

```bash
pip3 freeze > requirements.txt
```

2: **Create** a Procfile with the following command.

```bash
echo web: python3 app.py > Procfile
```

3: **Push** these newly created files to your repository.
4: **Create** a new app for this project on the Heroku Dashboard.
5: **Select** your **deployment** method by clicking on the **deployment** method button and select GitHub.
6: On the dashboard, **set** the following config variables:

**Key**|**Value**
:-----:|:-----:
IP|0.0.0.0
PORT|5000
MONGO\_URI|mongodb+srv://<username>:<password>@<cluster\_name>-qtxun.mongodb.net/<database\_name>?retryWrites=true&w=majority
SECRET\_KEY|"your\_secret\_key"

7: Click the deploy button on the Heroku dashboard.
8: The site has been deployed the Heroku.

[Back to content](#contents)

---

## Credits ##

### Images ###

### Image editing ###

- I have used the snippet tool for capturing screengrabs which I saved as images.
- MS Paint 3D to edit images as required.
- A handy [Birme](https://www.birme.net/?target_width=300&target_height=300&quality=100&border_width=1&border_color=%23bd3d3a) site allowed me to resize the images all at once.

### Code ideas ###

- To enable better understanding on how to plan database design, I have [referred to](https://github.com/Geomint/beer-time) the fellow student project.


[Back to content](#contents)

---

## Acknowledgements ##

[Back to content](#contents)

---