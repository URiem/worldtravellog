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
  - [Manual Testing](#manual-testing-bdd)
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
<img src="static/media/docs/py_test_asgi.png" width="60%">
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

- Chrome
- Edge
- Safari
- Waterfox

# Bugs and Fixes

:arrow_left: [Return to the README](README.md)
