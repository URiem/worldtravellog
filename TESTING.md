# The WorldTravel Log Testing

:arrow_left: [Return to the README](README.md)

## Table of Contents

- [Performance](#performance)
- [Accessibility](#accessibility)
- [Code Validation](#code-validation)
  - [HTML Validation](#html-validation)
  - [CSS Validation](#css-validation)
  - [JS Validation](#js-validation)
  - [PEP8 Validation](#python-code-validation)
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [Automated Testing](#automated-testing)
- [Browser Testing](#browser-testing)
- [Bugs & Fixes](#bugs-and-fixes)

# Performance

[Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) was used to test the performance of the website.

<details>
<summary>Desktop</summary>

- Home page

  <img src="static/docs/lighthouse_test_mainpage.png" width="60%">

- Entry Detail page

  <img src="static/docs/lighthouse_test_entrydetail.png" width="60%">

</details>

<details>
<summary>Mobile</summary>

- Home page

  <img src="static/docs/#.png" width="60%">

- Entry Detail page

  <img src="static/docs/#.png" width="60%">

</details>

# Accessibility

The [WAVE WebAIM web accessibility evaluation tool](https://wave.webaim.org/) was used to ensure the website met high accessibility standards.

**Wave results:**

<details>
<summary>Home page</summary>
<img src="static/docs/accessibility_test_wave.png" width="30%">
</details>

# Code Validation

## HTML Validation

The [W3C Markup Validation Service](https://validator.w3.org/) was used to validate the HTML of the website.

**HTML results:**

The following pages where tested and no errors were detected on any of the pages.

<details>
<summary>Home page</summary>
<img src="static/docs/html_test_home.png" width="60%">
</details>
<details>
<summary>Log Entry Detail page</summary>
<img src="static/docs/html_test_entrydetail.png" width="60%">
</details>
<details>
<summary>Login page</summary>
<img src="static/docs/html_test_login.png" width="60%">
</details>
<details>
<summary>Sign Up page</summary>
<img src="static/docs/html_test_signup.png" width="60%">
</details>
<details>
<summary>Logout page</summary>
<img src="static/docs/html_test_logout.png" width="60%">
</details>
<details>
<details>
<summary>Add Logentry page</summary>
<img src="static/docs/html_test_addlogentry.png" width="60%">
</details>
<summary>Update Logentry page</summary>
<img src="static/docs/html_test_updatelogentry.png" width="60%">
</details>
<details>
<summary>Delete Logentry page</summary>
<img src="static/docs/html_test_deleteentry.png" width="60%">
</details>
<details>
<summary>User Entries page</summary>
<img src="static/docs/html_test_userentries.png" width="60%">
</details>
<details>
<summary>Countries page</summary>
<img src="static/docs/html_test_countries.png" width="60%">
</details>

## CSS Validation

The [W3C Jigsaw CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to validate the CSS of the website.

The testing of the `style.css` file resulted in the following outcome:

<img src="static/docs/css_test_cssfile.png" width="50%">

## JS Validation

[JSHint](https://jshint.com/) was used to validate the JavaScript/Jquery of the website.

## Python Code Validation

The python code was tested using the [CI Python Linter](https://pep8ci.herokuapp.com/).

**Python testing results Travellog App:**

<details>
<summary>models.py</summary>
<img src="static/docs/py_test_models.png" width="60%">
</details>
<details>
<summary>views.py</summary>
<img src="static/docs/py_test_views_travellog.png" width="60%">
</details>
<details>
<summary>forms.py</summary>
<img src="static/docs/py_test_form.png" width="60%">
</details>
<details>
<summary>urls.py</summary>
<img src="static/docs/py_test_urls_travellog.png" width="60%">
</details>
<details>
<summary>apps.py</summary>
<img src="static/docs/py_test_app.png" width="60%">
</details>
<details>
<summary>admin.py</summary>
<img src="static/docs/py_test_admin.png" width="60%">
</details>

**Python testing results of Worldtravels Files:**

<details>
<summary>views.py</summary>
<img src="static/docs/py_test_views_worldtravel.png" width="60%">
</details>
<details>
<summary>asgi.py</summary>
<img src="static/docs/py_test_asgi.png" width="60%">
</details>
<details>
<summary>wsgi.py</summary>
<img src="static/docs/py_test_wsgi.png" width="60%">
</details>
<details>
<summary>urls.py</summary>
<img src="static/docs/py_test_urls_worldtravel.png" width="60%">
</details>

# Testing

## Manual Testing

BDD, or Behaviour Driven Development, is the process used to test user stories in a non-technical way, allowing anyone to test the features of an app.

**EPIC: Content and navigation**
| ID | User Story | Action/Expected Results | Pass |
| -- | ---------- | ----------------------- | ---- |
| 1A | As a user, I want to see a navigation menu so I can easily movement through the site. | A user accessing any page on the site will see a navigation bar in the header with links to the core pages of the site. Click on a desired link and a new page opens. On a mobile devise or other small screens a burger menu can be clicked and the menu will appear. | :white_check_mark: |
| 1B | As a user, I want to see relevant information about the site and its content easily so I can decide if I want to register an account | For unregistered users who access the home page a hero image and banner with a call to action succinctly invokes the purpose of the site. Trip entries displayed in a list below the hero image illustrate the purpose. | :white_check_mark: |
| 1C | As a user, I want to see an intuitive and visualy pleasing design that matches the intent of the website. | Access any of the core pages of the site. They will display a list of relevant log entries in uncluttered and clear styling, illustrating the intent of the page. | :white_check_mark: |
| 1D | As a user, I can access different pages on the site, so that I can navigate smoothy through all the functionality of the site. | Any user can scroll to the top of any page to access the header. In the header clear navigation options are displayed to the core pages of the site. The site is clearly divided into pages that perform distinctly different functionalities. | :white_check_mark: |

**EPIC: REGISTRATION AND USER**
| ID | User Story | Action/Expected Results | Pass |
| -- | ---------- | ----------------------- | ---- |
| 2A | As a user, I want to be able to register a profile, so I can access the main functionality of the site. | An unregistered user will see a 'Register' link in the navigation bar when scrolling to the top of the home page, click on this and a page opens which allows the user to register an account. | :white_check_mark: |
| 2B | As a user, I want to be able to log into my account easily, so I can access my account information. | An unregistered user will see a 'Login' link in the navigation bar when scrolling to the top of the home page, click on this and a page opens which allows the user to log in. | :white_check_mark: |
| 2C | As a user, I want to be able to logout of my account with ease to protect my account information. | A registered user will see a 'Log out' link in the navigation bar when scrolling to the top of the home page, click on this and a page opens which will request confirmation from the user to log out. | :white_check_mark: |

**EPIC: MANAGING LOG ENTRIES**
| ID | User Story | Action/Expected Results | Pass |
| -- | ---------- | ----------------------- | ---- |
| 3A | As an authenticated user, I want to be able to add a log entry and choose privacy and draft/publish setting, so that I can create a trip log that displays as specified on the site. | As an authenticated user, I can access a link in the navigation bar called 'Add a Trip', click on this and a page will open that displays a form with several fields including privacy and publish/draft choices and a 'submit' button, allowing the user to add and display a log entry to their account. | :white_check_mark: |
| 3B | As an authenticated user, I want to be able to edit and delete my log entries so that I can customize as I see fit. | An authenticated user can click on 'My Trips' in the navigation bar, locate the entry they wish to edit, click on it, to open the entry in the detail view. Here the user will be able to see two buttons under the entry description, one to update and one to delete the view. Click on the relevant choice and either a form will be displayed in a new page allowing the user to edit the entry information, or a confirmation screen is displayed requesting confirmation to delete the entry from the user. | :white_check_mark: |
| 3C | As an authenticated user, I want to be able to add images to individual log entries so that I can customize the log entry with this added feature. | An authenticated user can click on 'My Trips' in the navigation bar, locate the entry they wish to add images to, click on it, to open the entry in the detail view. At the bottom of the entry a form will be displayed allowing the user to add images to the specific log entry. | :white_check_mark: |
| 3D | As an authenticated user, I want to be able to delete the images associated with a particular log entry so that I can customize individual entries. | An authenticated user can click on 'My Trips' in the navigation bar, locate the entry the images of which they wish edit, click on it, to open the entry in the detail view. Each image in the Trip Gallery will have a small wastebasket icon next to the caption of the image, which the user can click to delete the image. | :white_check_mark: |

**EPIC: USER VIEWS**
| ID | User Story | Action/Expected Results | Pass |
| -- | ---------- | ----------------------- | ---- |
| 4A | As a user, I want to be able to see all publically available log entries so that I can browse through them. | Here is what I do to make this happen | :white_check_mark: |
| 4B | As a user, I want to be able to view the detail of all publically available log entries, so I can learn details about the trip entry. | Here is what I do to make this happen | :white_check_mark: |
| 4C | As a user, I want to be able to search the log entries by country, in order to see various trips associated with that country. | Here is what I do to make this happen | :white_check_mark: |
| 4D | As an authenticated user, I want to be able to view all my personal entries including the current settings on privacy and published/draft status so that I can get a quick overview of my entries | Here is what I do to make this happen | :white_check_mark: |
| 4E | As an authenticated user, I want to see feedback on my interactions with the site functionality, so that I can confirm my intended action was executed correctly. | Here is what I do to make this happen | :white_check_mark: |

## Automated Testing

Based on testing guidance and instruction on the Code Institute LMS 'Hello Django' walkthrough some automated testing for the project was carried out. Three separate files where used `test_models.py` to test some aspects of the models, `test_views.py` to test aspects of the views, and `test_forms.py` to test the forms.

In addition the following website were used for guidance and trouble shooting on how to implement the automated testing:

- https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing
- https://www.valentinog.com/blog/testing-modelform/
- https://cferreirasuazo.medium.com/lets-unit-test-django-forms-280704168d1b
- https://github.com/cloudinary/pycloudinary/blob/master/django_tests/test_cloudinaryField.py
- https://stackoverflow.com/questions/26298821/django-testing-model-with-imagefield#26307916
- https://github.com/useriasminna/italianissimo-booking-website/blob/main/booking/tests.py

**Testing results:**

- **test_models.py**

<img src="static/docs/at_test_models.png">

- **test_views.py**

<img src="static/docs/at_test_views.png">

- **test_forms.py**

<img src="static/docs/at_test_forms.png">

**Testing coverage:**

A coverage report was generated to determine the percentage of code tested:

<img src="static/docs/automated_testing_coverage.png">

# Browser Testing

The application was tested on the following browsers and worked without issues:

- Chrome
- Edge
- Safari
- Waterfox

# Bugs and Fixes

:arrow_left: [Return to the README](README.md)
