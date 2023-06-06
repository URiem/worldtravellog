# The WorldTravel Log

(Developer: Ulrike Riemenschneider)

![Mockup image](#)

**Live Site:**

[Live webpage](https://worldtravels.herokuapp.com/)

**Link to Repository:**

[Repository](https://github.com/URiem/worldtravellog)

**Developed by: Ulrike Riemenschneider**

## Table of Content

- [The WorldTravel Log](#the-worldtravel-log)
  - [Table of Content](#table-of-content)
  - [Introduction](#introduction)
    - [Project Goals](#project-goals)
    - [Data Base Design](#data-base-design)
  - [User Experience - UX](#user-experience---ux)
    - [Strategy](#strategy)
      - [Target Audience](#target-audience)
      - [User Requirements and Expectations](#user-requirements-and-expectations)
    - [Scope](#scope)
      - [Intial Stage](#intial-stage)
      - [Future Additions](#future-additions)
    - [Structure](#structure)
      - [Wireframes](#wireframes)
    - [Skeleton](#skeleton)
    - [Surface](#surface)
      - [Color Scheme](#color-scheme)
      - [Font](#font)
  - [Agile Development](#agile-development)
  - [Features](#features)
    - [Welcome Section](#welcome-section)
    - [Choose A Level Section](#choose-a-level-section)
    - [Quiz Section](#quiz-section)
    - [End of Game page](#end-of-game-page)
    - [Header](#header)
    - [Footer](#footer)
  - [Future Features](#future-features)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks \& Tools](#frameworks--tools)
    - [Helpful sites](#helpful-sites)
  - [Testing and Validation](#testing-and-validation)
    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
    - [JavaScript Validation](#javascript-validation)
    - [Accessibility \& Performance](#accessibility--performance)
    - [Browser Compatability](#browser-compatability)
    - [Testing User Stories](#testing-user-stories)
    - [Outstanding Issues](#outstanding-issues)
  - [Bugs \& Fixes](#bugs--fixes)
  - [Deployment \& Development](#deployment--development)
  - [Credits](#credits)
    - [Media](#media)
    - [Code](#code)
  - [Content](#content)
  - [Acknowledgements](#acknowledgements)

## Introduction

The WorldTravel Log is a website that is designed to allow users to upload and keep track of information on travels they have undertaken. Each 'Travel Log Entry' contains information on one particular trip and the user can then opt to add additional images to the log of each particular trip. Users can set up accounts which allows them to add, edit and delete entries as well as images associated with each entry. Users can also choose to give an entry a privacy setting so that only they will be able to view it and it will not be shared for all users to see. 

The project was desiged as the 4th portfolio project of the Code Institutes Full Stack Diploma Program. It was built using Django, Python, JS, CSS and HTML.

### Project Goals

The goal of the project was to build a tool for users to create a repository of memories from travels so that they may share them with others, privately or publically, or use them like a small photo diary of experiences. Each travel log can be populated with a small gallery of pictures from memorable moments of the adventures. So often images from our travel sit in file structures on private computers and are seldom looked at. If shared on common social media site, they disappear in a long, long timeline of social media posts that are difficult to search for or retrieve in the future. This site allows users to create log entries focusing on a specific trip, with a short description and defining information, such as the country of travel, the year and a descriptive title. The log entries can be edited and deleted by the user who created them. To protect their privacy, users can choose if they wish to publically share a log entry or keep it private.

### Data Base Design

The Entity Relationship Diagram (ERD) illustrates the structure of the data base which lies at the core of the functionality of the site:

![EDR](/static/media/images/erd.jpeg)

A User Model is provided by Django, a Logentry Model stores the details of each Triplog that a user adds, a user can add many log entries. An Image Model allows the user to add and store images specific to each Triplog, each Log can have multiple pictures associated with it. In addition a Country Model allows the user to categorize their entries by country of travel, which then makes the log entries searchable to the user.

## User Experience - UX

### Strategy

#### Target Audience

#### User Requirements and Expectations

- Simple and intuitive navigation system.
- Links work as expected.
- Immediate feedback on progress.
- Visually appealing responsive design.
- Accessibility.

### Scope

#### Intial Stage

#### Future Additions

### Structure

#### Wireframes

1. **Home Page**

![Home Page](#)

2. **Logentry Detail Page**

![Logentry Detail](#)

3. **404 Page** - a simple 404 Error page is also included (404.html)

### Skeleton

### Surface

#### Color Scheme

![Color Scheme](#)

#### Font

## Agile Development

Table of Epics, Userstories, Tasks etc.

## Features

### Welcome Section

### Choose A Level Section

### Quiz Section

### End of Game page

### Header

### Footer

## Future Features

## Technologies Used

### Languages

- HTML
- CSS
- JavaScript
- Python

### Frameworks & Tools

- Django
- Git
- GitHub
- Gitpod
- Balsamiq
- Google Fonts
- Font Awesome
- Coolors.co

### Helpful sites

Several sites came in handy while developing the code to help with problem solving:

- <a href="https://www.w3schools.com/">W3 Schools</a>
- <a href="https://stackoverflow.com">Stack Overflow</a>
- <a href="https://developer.mozilla.org/">mdn web docs</a>

## Testing and Validation

### HTML Validation

### CSS Validation

### JavaScript Validation

### Accessibility & Performance

### Browser Compatability

The websites compatability was tested on the following browsers:

- Google Chrome
- Mozilla Waterfox
- Microsoft Edge
- Safari

### Testing User Stories

### Outstanding Issues

## Bugs & Fixes

| **Bug** | **Fix** |
| ----------- | ----------- |

## Deployment & Development

## Credits

### Media

Images not referenced below are owned by the developer.

Images:
- Background image by <a href="https://unsplash.com/@drwmrk">Andrew Stutesman</a> on <a href="https://unsplash.com/photos/l68Z6eF2peA">Unsplash</a>

### Code

Resources and inspiration came from a few sources:

Django Image Gallery Website Step by Step Tutorial <https://www.youtube.com/watch?v=eOM4e6N7fuc>

## Content

## Acknowledgements

I would like to thank:

- My mentor Brian O'Hare for his feedback, advice, guidance and support.
- Cohort fascilitator Paul Thomas O'Rirodan, for his general advice on the management of the course and pointing us to a plethora of resources to help with the projects.
- My husband, Matt, for his encouragement and support along the way.
