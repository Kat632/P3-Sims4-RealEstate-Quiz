# The Sims 4 Real Estate Quiz

## Introduction

The Sims 4 Real Estate Quiz is a browser-based game built in Python.  It is a game based on the incredibly popular Sims 4 game.

The Sims 4 has a massive online community fan base, with hundreds of Youtube channels dedicated to playing the game.  BuzzFeed has quizzes for fans of the Sims to test their game knowledge, find out which townie they are most like, etc... https://www.buzzfeed.com/search?q=the%2Bsims&type=quiz ... so I thought it would be a fun idea to build a Sims 4 Real Estate Quiz for my project.  As far as I have been able to ascertain, no one has ever built a quiz based on Sims 4 real estate before, so actually I think my idea is quite unique.  

As the game was developed in Python for use in the terminal, it utilises the Code Institute Python Template to generate a "terminal" onto the page, making it available within a web browser.

![Screenshot of homepage]()

[View the live website on Heroku]()
Please note: To open any links in this document in a new browser tab, please press CTRL + Click.

## Table of Contents
* [User Experience Design (UX)](#UX)
    * [The Strategy Plane](#The-Strategy-Plane)
        * [Site Goals](#Site-Goals)
        * [User Stories](#User-Stories)
    * [The Scope Plane](#The-Scope-Plane)
    * [The Structure Plane](#The-Structure-Plane)
        * [Opportunities](#Opportunities)
    * [The Skeleton Plane](#The-Skeleton-Plane)
        * [Wireframes](#Wireframe-mockups)
        * [Logic Flow](#Logic-flow)
    * [The Surface Plane](#The-Surface-Plane)
* [Features](#features)
* [Future Enhancements](#future-enhancements)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## UX
### The Strategy Plane

* The Sims 4 Real Estate Quiz is intended to be a fun quiz to test a user's knowledge of who lives where and with whom at the start of a new game in the Sims 4.  At the start of a new game in Sims 4, most of the worlds are pre-populated with "Resident Townies" who live in pre-built houses.  This quiz is about those Sims and their houses.  This game is suitable for individual users looking to play a game for short or medium periods of time to test their knowledge of the Sims. Given the limitations of the terminal-based interface, care will need to be taken to incorporate visual stimulus, along with an engaging narrative to convey an element of fun to the user. 

#### Site Goals

* To provide users with a fun quiz game to play.
* To provide users with a range of questions to test their knowledge.
* To provide users with the ability to record their scores and see how their knowledge compares to others.

### User Stories

* As a user I want an new quiz about the Sims 4 to play.
* As a user I want to be able to test my knowledge against other people.
* As a user I want to play a quiz that is unique.

### The Scope Plane

**Features planned:**
* As there are certain restrictions in the scope of the development of the application, such as the terminal confines and methods of deployment. It will be important to ensure all functionality is contained within the game terminal screen.
* Despite the confines of the terminal emulator, the site should site be visually stimulating and clear to the user that it is a game.
* The user needs to know what their score is.
* The user should be able to record their score on a leaderboard.

### The Structure Plane

User Story:

> As a user I want an new quiz about the Sims 4 to play.

Acceptance Criteria:
* It should be clear to the user that this is a quiz game about the Sims 4 and what they have to do in order to play the game.

Implementation:
* The layout, use of colour and in game narrative will all be designed to immerse the user. Conveying a sense of fun to the user throughout the interactions with the game. Instructions on how to play will be available at the start of the game, along with clear prompts and validation for each user input.

User Story:

> As a user I want to be able to test my knowledge against other people.

Acceptance Criteria:
* The user should be able to add their score to the leaderboard and they should be able to choose to view the whole leader board.

Implementation:
* The user will have the ability to choose to add their score to the leaderboard at the end of the game and they will also be given the option to view the leaderboard.  This may need to be limited to the top ten scores on the leaderboard. 

User Story:

> As a user I want to play a quiz that is unique.

Acceptance Criteria:
* The user should be able to play the game multiple times without having too many of the same questions repeated.  The quiz will have ten questions, but these will be randomised from a much bigger bank of questions.

Implementation:
* 
* The user will also have the ability to exit a game at any point without quitting the application. This will allow the user to further control the time within the game.

#### Opportunities

Arising from user stories
| Opportunities | Importance | Viability / Feasibility
| ------ | :------: | :------: |
| ** Provide a fun game environment ** | 5 | 5 |
| ** Provide different difficulty levels ** | 5 | 5 |
| ** Provide ability to control the time the game takes ** | 5 | 5 |

### The Skeleton Plane
#### Wireframe mock-ups

Given that the application will be run within a terminal emulator provided within the template, there are limited options available with regards to the layout of the webpage itself. Early on within the development of the theme, I located a suitable background graphic on iStock. To position the terminal appropriately for the background graphic, and keeping user experience in mind, I decided to centre the terminal horizontally on the screen. The run program button was centrally positioned to above the terminal window to emphasis its importance.

![Home Page Wireframe]()

For the terminal window itself, I also produced a wireframe in the well-known design package Microsoft Excel. Whilst not traditionally used for this purpose, the terminal window dimensions of 80 columns wide by 24 rows high provided a restriction that I could duplicate in excel easily. This enabled me to work out the spacing requirements and dimensions of the elements on screen during the gameplay. Given that all the elements that would be displayed in the terminal are ASCII characters, creating an 80 x 24 grid in excel with one character per tile it enabled me to easily see if I could fit the total information required on each line. This was especially useful whilst calculating how to print the two game boards with a scoreboard in between them, given the line-by-line method in which the terminal prints.

![Terminal Game Play Wireframe]()

#### Logic Flow

To begin to understand how I wanted the game to work, I prepared a couple of slides for my mentor and I in plain English.  I find it exceedingly helpful to plan in English before I start writing any code.  I used these slides to develop the logical flow of the game.

To develop the logical steps required within the game, along with gaining an understanding of how the different game elements would interact, I created a flow chart detailing the individual steps for the game. Given the scope of the game logic involved the full flow chart resulted in a large image. The full image can be viewed here [Logic Flow Diagram]()

The game logic can be broken down into three distinction sections. The initial setup of the game, answering the question and checking the result before moving on to the next question. For ease of reference, I have broken up the logic flow diagram into these three sections.

##### Setup Logic

![Setup Logic]()

##### Question Logic and Validation

![Question Logic]()

##### Game Loop Logic

![End of Game Logic]()

#### Programming Paradigm

I utilised an Object Orientated Programming approach to developing the game. One initial function will be utilised to establish the user's name. This data will then be used to establish the game instance. The game instance will be utilised to control the flow of the game, present data to the user and establish other objects as needed.

![Class Overview]()

What objects will I use?
What classes will I use?
What methods on each class to play the game?


I will utilise a variety of methods on each class to play the game. The Game class will contain methods for the general running of the game itself. The Player class will contain methods that will manipulate the data inputted by the user into game actions such as feedback about whether a question is correct or incorrect.

### The Surface Plane

#### Design

Once I was happy with the overall layout of the page, I created a full colour mock-up within Balsamiq.

![Full Colour Mock-up]()

## Features
#### Welcome Screen

![Welcome Screen](/assets/screenshots/welcome-screen.png)

At the start of game users are greeted with a welcome screen showing the game logo of a plumbob.  This is instantly recognisable to anyone who plays the Sims. The game asks the user if they would like to play a game, with instructions on how to start the game, or access the instructions.

#### Instructions Screen

![Instructions Screen]()

If users select the instructions option from the main menu the screen will display an overview of the story behind the game and the objective for the user. They are then presented the same message as the welcome screen asking if they would like to play a game.

#### Name Input Screen

![Name Input Screen]()

When the user confirms that they would like to play the game, they are greeted by a message asking them to input their name.

#### Game Screen

![Game Screen]()

Once the user has inputted their name, they are greeted on the next screen with a welcome message containing their name.

#### Questions Screen

![Questions Screen]()

The game will then progress to the questions, with the user required to press enter to start. Once the user has indicated that they are ready, the first question will display.

#### Correct Answer Screen

![Correct Answer Screen]()

If the user answers the question correctly, a message will be displayed informing them that they have answered correctly.  The user will also be informed of their current score.

#### Incorrect Answer Screen

![Incorrect Answer Screen]()

If the user answers incorrectly, a message will be display informing them that they have answered incorrectly. The user will also be informed of their current score.

#### End of Game Screen

![End of Game Screen]()

The user will be asked a total of ten questions.  At the end of ten questions, a screen will be displayed informing them of their final score.  The user will also be asked if they would like to input their score to the leaderboard, restart the game or exit the game.

#### Add score to Leaderboard Screen

![Add score to Leaderboard Screen]()

The user will be informed that their score is being added to the Leaderboard, then they will be asked if they wish to view the leaderboard, restart the game or exit the game.

#### Leaderboard

![Leaderboard]()

This screen will display the leaderboard to the user.  The user will then be asked if they wish to restart the game or exit the game.

#### Restart the game

![Restart the game]()

The user should not be prompted to input their user name again

#### Exit Game Screen

![Exit Game Screen]()

This will thank the user for playing the game and hope they come back soon.  Happy Simming!

## Future Enhancements

High scores - It would be a nice addition to the game to develop a scoring system which is based on the time it takes the user to answer each question.

## Testing

### Testing Strategy

I took a two-stage approach to testing the application. The first stage was continuous testing as the application was being developed. With the application being based within the terminal, it was straight forward to test functions and print statements as they were being developed using the terminal within the IDE. This involved writing functions and print statements to enable me to see check that the questions were being randomised correctly.

For the second stage of testing, I utilised a more formal structured approach and created a test schedule for the application which covered each logical cycle. I then proceeded to run through the manual tests I'd developed one at a time noting the result and recording any errors found. Where unexpected behaviour was encountered, the code was altered to correct the behaviour.

The individual python files were also validated using [pep8online.com](http://pep8online.com/) further details are below.

#### Testing Overview

Testing was divided into different sections to ensure everything was tested individually with test cases developed for each area.

![Testing Schedule Overview]()

A full detailed breakdown of the testing procedures and methodology can be found in the testing.md file [here](TESTING.md)

#### Validator Testing

* pep8online.com - I utilised [pep8online.com](http://pep8online.com/) to validate my python code. All python files were checked with no errors reported.


* Screenshots of the validator reports are here:
    * []()
    * []()
    * []()
    * []()
    * []()
    * []()
    * []()
    * []()
    * []()
    * []()

#### Notable Bugs



#### Libraries Utilised
##### Built in Python Libraries

Several of the built in python libraries were utilised to enable additional functionality within the application.
##### math ???

##### time
The time library was imported to utilise the time.sleep functionality. This enabled me to incorporate specific time delays within the program which adds to the player experience by simulating the time between the player's answer and the computers response. Whilst only a small time delay occurs, I felt that it was a much better experience than the computer response appearing as soon as the user has pressed their answer key. 
##### os
The os library was imported to utilise the os.system and os.name functionality. This enabled me to add functionality to the terminal emulator which allowed me to clear the previous print statements. This provides a clearer and more structured experience for the user.
##### random
The random library was imported to access a number of the built in methods of generating a random selection.
##### string ???
.

## Deployment

The site was deployed via Heroku, and the live link can be found here - [Game]()

The project was developed utilising a Code Institute provided template.

### Project Deployment

To deploy the project through Heroku I followed these steps:
* Sign up / Log in to [Heroku](https://www.heroku.com/)
* From the main Heroku Dashboard page select 'New' and then 'Create New App'
* Give the project a name - I entered Calcio-Jack and select a suitable region, then select create app. The name for the app must be unique.
* This will create the app within Heroku and bring you to the deploy tab. From the submenu at the top, navigate to the settings tab.
* This next step is required for creating the app when using the CI Python Deployment Template. If you created your own program without using the CI Template, you might not need to add a config var.
* In the config vars section select the reveal config vars button. This will display the current config vars for the app, there should be nothing already there.
* In the KEY input field input PORT all in capitals, then in the VALUE field input 8000 and select the Add button to the right.
* Next select the add buildpack button below the config vars section.
* In the pop-up window select Python as your first build pack and select save changes.
* Then repeat the steps to add a node.js buildpack.
* The order of the buildpacks is important, in the list Python should be first with Node.js second. If they are not in this order, you can click and drag them to rearrange.
* Next navigate back to the deploy tab using the submenu at the top of the page.
* In the deployment method section select the GitHub - Connect to GitHub button and follow the steps prompted if any to connect your GitHub account
* In the Connect to GitHub section that appears, select the correct account, and enter the name of the repository and select search.
* Once Heroku has located the repo select connect.
* This will connect the repo to the app within Heroku. Below the Apps Connected to Heroku section will be the Automatic Deploys section.
* In this section, confirm the correct branch of the repo is selected in the drop-down box, and then click the Enable Automatic Deploys button
* This will ensure whenever you change something in the repo and push the changes to GitHub, Heroku will rebuild the app. If you prefer to do this manually you can utilise the manual deployment options further down. For this project I utilised the Automatic Deployment to enable me to check changes I made to the app as I developed it.
* Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.

## Credits

### Code

I was informed of a method to clear the terminal by another student on the course Goran Sigeskog who had found the method in a Python cheat sheet provided by [coding4you](http://www.coding4you.at/inf_tag/beginners_python_cheat_sheet.pdf). Goran had used the method successfully within his project. The code is credited within the editscreen.py file. Goran's GitHub can be found [here](https://github.com/gorsig).

#### Difficulty Levels



### Content

#### Background Image

The background image was chosen from a selection of Sims 4 wallpapers at [Wallpaper Access](https://wallpaperaccess.com/the-sims-4#google_vignette).  I chose this image because it is instantly recognisable as being related to the Sims 4.


#### Stack Overflow



#### Haoyi's Programming Blog

Whilst further researching utilising different colours within the terminal I discovered Haoyi's programming blog. Whilst ultimately, I did not use the techniques detailed in the finished app, it did provide me with several ideas on how I could incorporate colours within the terminal. It is worth a read if you are looking at animating or using colour within a terminal window and can be found [here](https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html)

#### Wikipedia

Wikipedia was used as a reference point for details of the Sims franchise and details of the various worlds and neighbourhoods in the Sims 4. [The Sims 4](https://en.wikipedia.org/wiki/The_Sims_4)

#### ASCII Art

The image used to make the ASCII art was downloaded from [ClipArtMax](https://www.clipartmax.com/max/m2H7d3N4K9K9b1H7/).

The program used to convert the image into ASCII art is at [Many Tools](https://manytools.org/hacker-tools/convert-images-to-ascii-art/)

### Acknowledgements

I'd like to thank the following:
* 
* 
* 
