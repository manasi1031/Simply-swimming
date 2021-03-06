# Milestone Project 4
---------
# Simply Swimming

![Single Mockup Image](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/single-view-screenshot.png)

## Purpose
---
This site has been designed as a Full-Stack site based on business logic used to control a centrally-owned dataset. This is the fourth milestone project in my academic schedule with the Code Institute. 

## Information about project: 
---

Simply Swimming is a company that offers swiming lessons / classes to different age groups and can cater to different requirements. They have the trained staff who are also offer bespoke services.

This website can not be used as a template for a business since it's a project for educational purposes.

## [View live website here](https://simplyswimming.herokuapp.com/)

---------

## Table of Contents
---
- [UX](#ux)
    - [Goals](#goals)
        - [Vision](#vision)
        - [Aim](#aim)
        - [Target Audience](#target-audience)
        - [User Stories](#user-stories)
    - [Structure of the Website](#structure-of-the-website)
        - [Design](#design)
        - [Typography](#typography)
        - [Color Scheme](#color-scheme)
        - [Wireframes](#wireframes)
        - [Images](#images)
- [Features](#features)
    - [Database Structure](#database-structure)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
    - [Functionality Testing](#functionality-testing)
    - [Compatibility Testing](#compatibility-testing)
    - [User Testing Stories](#user-testing-stories)
    - [Code Validation](#code-validation)
    - [Issues found during deployment](#issues-found-during-deployment)
    - [Performance Testing](#performance-testing)
- [Deployment](#deployment)
- [Credits](#credits)
- [Screen Shots](#screen-shots)

---------
## UX
---
### Goals
---
The main reason to create this website is people to be aware of the services we offer and where we are located.

#### Vision 

To be the best swimming school in Ockendon while offering services to cater to all groups of people.

#### Aim

My aim is to provide data relevant to the user story and enhance the overall visual experience.

#### Target Audience 

All types starting from babies to adults.

#### User Stories

##### Visitors Or Users:

- I want to know where the swimming class is located.
- I want to know the hours that the location is open.
- I want to see what kind of courses the swimming class offers.
- I want to be able to make a booking.
- I want to be able to cancel an booking. 
- I want to know a bit more about the company / trainers. 
- I want to be able to contact the company with random questions. 
- I want to get a confirmation email with my booking time. 

##### Site Owner:

- I want to show where the swimming class is located. 
- I want to let people see the courses we offer.
- I want to make it easy for customer to make an booking. 
- I want to get an email when someone makes a new booking. 
- I want to be able to confirm bookings.
- I want to be able to cancel bookings.
- I want to be able to change an booking date. 
- I want to have a clear overview of the customers details. 
- I want to be able to get email from customers through a contact form with any random questions.

[Back to Table of Contents](#table-of-contents)

----------
### Structure of the website
---

#### Design

The website is designed to be easy and user-friendy on all type of devices. On desktop, tablet or mobile device there should be no difference for a user to have a fantastic experience. All parts are designed to achieve maximum user satisfaction. 

#### Typography

The below 2 font families have been used for my website mainly:

- font-family: 'Open Sans', sans-serif; 

#### Color scheme

I used the palette maker from the [Coolors](https://coolors.co/image-picker) website based on the hero image chosen for the index.html page. 

This palette has been derived from the hero image and a [visual representation](https://github.com/manasi1031/Simply-swimming/blob/master/media/images/collage.png)

Colors chosen are either direct colors or in the palette shades to give a better effect as below: 
- HTML Background: #D2CF43
- Font: #000202

[Click here to view Color Palette](https://github.com/manasi1031/Simply-swimming/blob/main/media/documents/color-palette.pdf) 

#### Wireframes

Balsamiq has been used to create wireframes for this project.

- [Wireframes overview pdf file](https://github.com/manasi1031/Simply-swimming/blob/main/media/documents/overview-wireframe.pdf)

- [Laptop view of Home page](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/home-laptop-view.png)

- [Laptop view of About page](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/about-laptop-view.png)

#### Images

Images were sourced from pixabay.com and credit section has also been updated accordingly.

[Back to Table of Contents](#table-of-contents)

--------

### Features
---

The website consists of 6 pages that are accessible at the moment.

#### The website has below features:

NAVIGATION BAR
- The navigation bar is located on the top of each page and is fixed in location.
- The company name is the fixed logo and has a hyperlink to the home page.
- The navbar is fully responsive of different screen sizes.
- A confirmation message is on the screen when the user logs in or logs out. This disappears after 3 seconds automatically.

![Navbar generic user view](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/navbar-general.png)

![Navbar small screen view](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/navbar-small-screen-view.png)

![Navbar admin or signed in user view](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/navbar-signed-in-view.png)

COURSES SECTION
- On the home page, the courses section is just a basic overview of an image and a brief line of what it does.
- When you hover the mouse over a specific course, it will highlight itself and enlarge slightly to show that you prefer to view this on.
- When you click on the selected course, it takes you to a detailed page about that specific course.
- Moving forward there will be an option to make a new booking or view existing booking (Currently not setup).

![Courses Overview](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/courses-overview.png)

![Courses Detailed View](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/courses-detailed-view.png)

ABOUT US PAGE
- This page tell more information about the founder of the website and how the company was created.
- This page will also have a coaches section that will show the team that will be teaching or training people (Currently not setup).

![About Us View](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/about-us-feature.png)

FOOTER
- The footer is fixed for all pages
- This gives the information about the location, contact number and e-mail address for the company.
- Apart from this, it also specify the hours of operation.

![Footer View](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/footer.png)

CONTACT US PAGE
- The page gives a form for people to input their queries and sends to the website e-mail address to look into. 

![Contact page form](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/contact-us-feature.png)

LOGIN PAGE
- This page is for existing members to login in by adding their username and password to view their profile and bookings.

![Login Page](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/sign-in-feature.png)

SIGN UP PAGE
-  This is for new users to register themselves and asks for username, email address (optional) along with password and re-enter password for validation.

![Sign up page](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/register-feature.png)

SIGN OUT PAGE
- This page prompts you to log out by clicking on a button again and exists the member or user profile.

![Sign out page](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/sign-in-feature.png)


#### Features Left to Implement and will be in future versions:

- Coaches list on about page (Wrote code but was unable to fix error).
- Booking form page.
- Online member profiles to view.
- Make bookings or changes to existing user bookings.
- Make payments online.
- A Calendar on the create booking page for logged in users which shows which days are booked and which are available for booking. 


---
### Database Structure
---

COURSE MODEL

![Course Model](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/course-model.png)

[Back to Table of Contents](#table-of-contents)

-------
### Technologies Used
---------

Languages used:

- Programming Languages:
    - HTML5:  Used to write the structure of the website.
    - CCS3 & Bootstrap: Used to style the website.
    - Javascript: Used to allow users to interact with web pages.
    - Python and Django framework

- Google fonts: Used as a font resource.

- Database framework: Postgres / Sql lite

- Balsamiq: Used to create wireframes.

- Git: Used as a version control system tracking.

- Gitpod: Used as a hosting platform.

- Github: Used as a platform to keep project in a remote server.

- Google Chrome DevTools: Used for testing responsiveness and solving any problems.

- HTML Validator: Used for validating HTML code.

- CSS Validator: Used for validating CSS code.

- [PNG to JPG](https://png2jpg.com/) to convert png files to jpg.

- [Favicon Generator](https://favicon.io/favicon-generator/) to generate favicon for website.

[Back to Table of Contents](#table-of-contents)

--------

### Testing 
--------

#### Functionality Testing:

I used Google Chrome DevTools to check the responsiveness of the web page on different devices and rectified problems accordingly.

#### Compatibility testing:

Site was tested in various devices on the Google chrome DevTools, however apart from this, physically checked in Moto G4, Redmi Note 5 Pro, Ipad Air, Ipad Air2 and Iphone 11 for different software's.

#### User Testing Stories:

I planned the project on a kanban board with user stories that can be viewed on this [link](https://github.com/manasi1031/Simply-swimming/projects/1)
There are a few that are still work in progress and few that are planned for future versions.

#### Code Validation:

At the and of the project I used the below websites to validate the codes and they all tested fine.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) to validate CSS.
- [W3C Html Validator](https://validator.w3.org/) to test HTML.
- [PEP8 online tool](http://pep8online.com/) to test python code.
    - Most of the pylint was rectified, however the "too long line" errors were ignored to avoid the code breaking.

#### Issues found during deployment:

1. Testing database error

![testing-database-error](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/testing-database-error.png)

I was having the above error when I was testing my apps and after checking with Slack overflow solutions I still did not get this working. Post which i had a chat with tutor support and I was guided to the fact that I did not have permission to create a database with the way my settings were.

So whenever I had to get a testing done, I would go to env.py and comment out the line with the database settings and it worked. See the commented out section only when I had to do the tests.

![env.py-commentout](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/env.py-commentout.png)


2. Message alert feature not able to discard on its own

![Message alert feature](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/message-alert-feature.png)

When I added the message alerts to the sign in, sign out, log out and contact forms, the alerts remained for the whole duration unless I clicked it to close. I had to add in javascript code to get this sorted and I had to refer back to the code Institute "messages" section in the "I think therefore I blog" section.

![Messages javascript](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/messages-javascript.png)

3. Courses view error on index. html

![Courses view error](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/courses-view-error.png)

I had the above error that after using bootstrap the view on the page was still not aligned.
I could not find a bootstrap solution to this and added CSS styles as below:

- .link-course {
    text-decoration: none;
    color: inherit;
    text-align: center;
}

- .link-course:hover {
    color: inherit;
}

- .card-course:hover {
    transform: scale(1.05);
}

- .card-course {
    transition: transform 0.2s ease;
    box-shadow: 0 4px 6px 0 rgba(22, 22, 26, 0.18);
    border-radius: 0;
    border: 0;
    margin-bottom: 1.5em;
}

4. Courses image not veiwing error on courses_detail view

![Courses overview](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/courses-overview.png)

Once the courses app was working, the main view on the index.html was working but when I tried to view an individual course, the image was not showing up.
I used the below python code in courses.html and the error was rectified:

![Courses image pythoncode](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/courses-image-pythoncode.png)

5. Coaches data missing error

![Coaches data missing error](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/coaches-data-missing-error.png)

I created the coaches app but the above error still shows due to the fact the the error on the console was "The coach model does not contain any objects"
I tried looking for different options to help me online but could not resole this and hence left this for as a commented out section for now.
On the website it states details coming soon as a future feature.

6. Heroku depoloyed site CSS error

![Heroku deployed site CSS error](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/heroku-deployedsite-css-error.png)

The above error resulted from the fact that my CSS had a line in base.html header and I had used this - type="text/css".
Once I removed this, changed debug to "False" and added X_FRAME_OPTIONS = 'SAMEORIGIN' in setting.py, this worked. the error was resolved.

7. Heroku site deployment error

I did not take a visaul of the picture, however it mentioned that something was wrong and I could not deploy the site correctly. This resulted from the fact that my booking app with sendgrid was not setup correctly.
I have commented out the booking app and sendgrid code for now to get this up and running as I was unable to resolve prior to submission.

#### Performance Testing:

LIGHTHOUSE
I used [Lighthouse](https://developers.google.com/web/tools/lighthouse/) tool for testing the performance of my website.

![Lighthouse overview](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/lighthouse-overview.JPG)

COVERAGE
I also used the coverage report and have taken visuals of the overall status on my apps:

![Coverage report part 1](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/coverage-report-part1.png)

![Coverage report part 2](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/coverage-report-part2.png)

![Manual Testing result on Gitpod terminal](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/manual-testing-result.png)

[Back to Table of Contents](#table-of-contents)


----------

### Deployment
----------

The project was deployed on GitHub Pages. I used Gitpod as a development environment where I commited all changes to git version control system. I used push command in Gitpod to save changes into GitHub.

#### To deploy a project I had to:
The project was deployed to GitHub Pages using the following steps, I used Gitpod as a development environment where I commited all changes to git version control system. I used the push command in Gitpod to save changes into GitHub. 
Deployment to Heroku 
Before creating a Heroku app make sure your project has these two files: 
- requirements.txt - You can create one by usingpip3 freeze --local > requirements.txt 
- Procfile - You can create one by using echo web:python run.py > Procfile 

Create application: 
   1. Navigate to Heroku's sitehere. (Note: Right click on link to open a new tab). 
   2. Register and/or Login as applicable. 
   3. Click on the new button in the top right and select "Create new app". 
   4. Enter the app name and region closest to you. 
   5. Click the create app button. 

Set environment variables: 
   1. Click on the settings tab and then click "Reveal config vars". 
   2. Config variables added throughout project: (add image of variables) 

Setting up database in deployment 
   1. Temporarily add theDATABASE_URLtosettings.py: 
      DATABASES = { 'default': dj_database_url.parse('your_postgres_database_url') } 
   2. Migrate the data from development to production version. 
       To migrate the database models in the project to the Postgres database you can use the following command: python3 manage.py migrate 
   3. You will then need a superuser for the Postgres database too. To create one you can use the
        following command: python3 manage.py createsuperuser 
   4. Remove the Postgres database URL from settings.py as this should not in any case be deployed to 
        GitHub for security reasons. 
   5. To connect your Heroku app to be deployed from a Github repository, you can follow these steps: 
       - Open the heroku app page on the deploy tab and select GitHub - Connect to GitHub. 
       - Sign into GitHub if not already. 
       - A prompt to find a Github repository to connect to will then be displayed. 
       - Enter the repository name for the project and click search. 
       - Once the repository has been found, click the connect button. 
   6. Once you have your GitHub repository connected, without leaving deploy tab: 
       - Under Automatic deploys section, choose the branch you want to deploy from and then click the "Enable Automatic Deploys" button. 
       - To deploy your app to Heroku click the "Deploy Branch" button. 

[Back to Table of Contents](#table-of-contents)

-------

### Credits
-----

#### Content & Credit

- I did refer to the "Blog and Django" sample project and lessons from Code institute to follow a step by step approach to this project

- I also refered to W3schools website for referring to Bootstrap usage - https://www.w3schools.com/bootstrap/bootstrap_examples.asp for changing the navbar options to right for login, register and logout pages.

- Original content ideas and related data for the swimming website taken from https://theswimschool.co.uk/ 

#### Media

All images obtained are non-copyrighted and can be used freely from [Pixabay](https://pixabay.com/)

### Acknowledgements

I could not have done this project without the guidance and confidence of my mentor - Adegbenga Adeye.

Last but not the least, I would like to thank [Code Institute](https://codeinstitute.net/) for their support.

[Back to Table of Contents](#table-of-contents)

------

## Screen Shots

![Home page view Screenshot](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/single-view-screenshot.png)

![About page view Screenshot](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/about-page.png)

![Contact page view Screenshot](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/contact-page.png)

![Courses view individual page view Screenshot](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/courseview-page.png)

![Login page view Screenshot](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/accounts-login-page.png)

![Logout page view Screenshot](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/accounts-logout-page.png)

![Register page view Screenshot](https://github.com/manasi1031/Simply-swimming/blob/main/media/images/accounts-signup-page.png)