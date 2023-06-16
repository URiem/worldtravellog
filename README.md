# The WorldTravel Log

(Developer: Ulrike Riemenschneider)

![Mockup image](#)

**Live Site:**

[Live webpage](https://worldtravellog.herokuapp.com/)

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

The project was desiged as the 4th portfolio project of the Code Institutes Full Stack Diploma Program. It was built using Django, Python, JS, CSS and HTML. The data are stored in a PostgeSQL database.

### Project Goals

The goal of the project was to build a tool for users to create a repository of memories from travels so that they may share them with others, privately or publically, or use them like a small photo diary of experiences. Each travel log can be populated with a small gallery of pictures from memorable moments of the adventures. So often images from travel experiences sit in file structures on private computers and are seldom looked at. If shared on common social media site, they disappear in a long, long timeline of social media posts that are difficult to search for or retrieve in the future. This site allows users to create log entries focusing on a specific trip, with a short description and defining information, such as the country of travel, the year and a descriptive title. The log entries can be edited and deleted by the user who created them. To protect their privacy, users can choose to publically share a log entry or keep it private.

### Data Base Design

The Entity Relationship Diagram (ERD) illustrates the structure of the data base which lies at the core of the functionality of the site:

![ERD](/static/media/images/erd.jpeg)

A User Model is provided by Django, a Logentry Model stores the details of each Triplog that a user adds, a user can add many log entries. An Image Model allows the user to add and store images specific to each Triplog, each Log can have multiple pictures associated with it. In addition a Country Model allows the user to categorize their entries by country of travel, which then makes the log entries searchable to the user.

## User Experience - UX

The application was developed taking the Five Planes of User Experience into consideration:

### Strategy

| EPIC                       | ID  | User Story                                                                                                                                                                                        |
| -------------------------- | --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CONTENT AND NAVIGATION** |     |                                                                                                                                                                                                   |
|                            | 1A  | As a user, I want to see a navigation menu so I can easily movement through the site.                                                                                                             |
|                            | 1B  | As a user, I want to see relevant information about the site and its content easily so I can decide if I want to register an account                                                              |
|                            | 1C  | As a user, I want to see an intitive and visualy pleasing design that matches the intent of the website.                                                                                          |
| **REGISTRATION AND USER**  |     |                                                                                                                                                                                                   |
|                            | 2A  | As a user, I want to be able to register a profile, so I can access the main functionality of the site.                                                                                           |
|                            | 2B  | As a user, I want to be able to log into my account easily, so I can access my account information.                                                                                               |
|                            | 2C  | As a user, I want to be able to logout of my account with ease to protect my account information.                                                                                                 |
|                            | 2D  | As a user, I want to be able to delete my account information or request account deletion from the website owner.                                                                                 |
| **MANAGING LOG ENTRIES**   |     |                                                                                                                                                                                                   |
|                            | 3A  | As an authenticated user, I want to be able to add a log entry and choose privacy and draft/publish setting, so that I can create a trip log that displays as specified on the site.              |
|                            | 3B  | As an authenticated user, I want to be able to edit and delete my log entries so that I can customize as I see fit.                                                                               |
|                            | 3C  | As an authenticated user, I want to be able to add images to individual log entries so that I can customize the log entry with this added feature.                                                |
|                            | 3D  | As an authenticated user, I want to be able to edit and delete the images associated with a particular log entry so that I can customize individual entries.                                      |
| **USER VIEWS**             |     |                                                                                                                                                                                                   |
|                            | 4A  | As a user, I want to be able to see all publically available log entries so that I can browse through them.                                                                                       |
|                            | 4B  | As a user, I want to be able to view the detail of all publically available log entries, so I can learn details about the trip entry.                                                             |
|                            | 4C  | As a user, I want to be able to search the log entries by country, in order to see various trips associated with that country.                                                                    |
|                            | 4D  | As an authenticated user, I want to be able to view all my personal entries including the current settings on privacy and published/draft status so that I can get a quick overview of my entries |
|                            | 4E  | As an authenticated user, I want to be able to select and save favorite log entries, so that I can save them and view them in a separate page.                                                    |
|                            | 4F  | As an authenticated user, I want to see feedback on my interactions with the site functionality, so that I can confirm my intended action was executed correctly.                                 |

#### Target Audience

The target audience is user who enjoy travelling and would like to record their experiences and impressions in succint form online in order to share them with the wider public or privately for they own future enjoyment.

#### User Requirements and Expectations

- Simple and intuitive navigation system and design.
- Easy access to all functionality of the site.
- All links and features work as expected.
- Immediate feedback on progress during interaction with site features.
- Visually appealing responsive design.
- Accessibility.

### Scope

**Simple and intuitive User Experience**

- Ensure navigation menu is easily accessible and functions as expected.
- Ensure page names match the intended content.
- Ensure the user gets visual feedback when navigating through the sites functionalities.
- Create a design that matches the intent of the page.

**Relevant content**

- Add information about the site's purpose to make its intent clear to the user.
- Feature user created content on the front page that help the new user understand the purpose of the site.

**Core Website Functionality**

- Implement a Log Entry Features that allow the user to interact with the site.
- Implement the registration/login/logout features for access to core site functionality.
- Implement a form for adding an entry to the log.
- Implement a feature to edit and delete a log entry.
- Implement a feature that allows the user to add/edit/delete images to a log entry.

**Responsiveness**

- Implement responsive design for smooth desktop, tablet and mobile device access.

### Structure

The website is divided into XXX pages with content depending on whether the user is authenticated or not.

#### Current/Initial Structure

- **Home Page** is visible to both types of users. It includes a list of publically shared trip logs for the user to browse. Unauthenticated users will also see a banner calling them to register, authenticated users will not see the banner.
- **Register Page** gives the user the opportunity to create an account in order to access the core functionality of the site.
- **Login/Logut Pages** allow the user to authenticate or logout of their account.
- **Add Log Entry Page** allows an authenticated user to add a logentry to their account.
- **User Entries Page** allows authenticated user to see all their logs including those with the private setting and those that have not yet been published and are just saved as a draft.
- **Log Entry Detail Page** allows the user to view all the details of a trip log, if they are authenticated and it is their own post they will see buttons that allow to access the edit or delete features. They will also see a feature for adding/editing/deleting images associated with the log entry.
- **Update Log Entry Page** displays a prepopulated entry log form and allows the user to edit their previous inputs.

#### Yet to be implemented/future pages

- **Favorite Entries Page** allows a user to select/save and display their favorite log entries from all publically published posts.

**Add a flowchart illustrating user navigation through the site.**

### Skeleton

#### Wireframes

The wireframes for the pages listed in the above [Structure](#structure) section follow:

1. **Home Page**

![Home Page](#)

2. **Logentry Detail Page**

![Logentry Detail](#)

3. **404 Page** - a simple 404 Error page is also included (404.html)

### Surface

#### Color Scheme

![Color Scheme](#)

#### Font

## Agile Development

All functionality and development of this project was managed through GitHub issues, milestones and projects.

### Sprints

- Sprint 1: Initial Set-up

- Sprint 2: Add user authentication

- Sprint 3: Add Log Entry feature

- Sprint 4: Create customized views

- Sprint 5: Refine and customize the CSS including footer and header

- Sprint 6: Testing

- Sprint 7: Final revisions to code and documentation

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
| ------- | ------- |

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
