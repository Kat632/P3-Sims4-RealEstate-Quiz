# The Sims 4 Real Estate Quiz

## Introduction

The Sims 4 Real Estate Quiz is a browser-based game built in Python.  It is a game based on the incredibly popular Sims 4 game.

The Sims 4 has a massive online community fan base, with hundreds of Youtube channels dedicated to playing the game.  [BuzzFeed](https://www.buzzfeed.com/search?q=the%2Bsims&type=quiz) has quizzes for fans of the Sims to test their game knowledge, find out which townie they are most like, etc... so I thought it would be a fun idea to build a Sims 4 Real Estate Quiz for my project.  As far as I have been able to ascertain, no one has ever built a quiz based on Sims 4 real estate before, so actually I think my idea is quite unique.  

As the game was developed in Python for use in the terminal, it utilises the Code Institute Python Template to generate a "terminal" onto the page, making it available within a web browser.

![Screenshot of homepage](/assets/amiresponsive.png)

[View the live website on Heroku](https://p3-sims4-realestate-quiz.onrender.com/)
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

* The Sims 4 Real Estate Quiz is intended to be a fun quiz to test a user's knowledge of who lives where and with whom at the start of a new game in the Sims 4.  At the start of a new game in Sims 4, most of the worlds are pre-populated with "Resident Townies" who live in pre-built houses.  This quiz is about those Sims and their houses.  This game is suitable for individual users looking to play a game for short or medium periods of time to test their knowledge of the Sims. Given the limitations of the terminal-based interface, care will need to be taken to incorporate visual stimulus, along with engaging questions that will be fun for any Sims player to answer.  A few of the questions are "faux-amis" meaning that the answer is not the obvious one and many questions will leave players of the Sims thinking, "Wow, I never knew that...", for example with the question about who lives in the cheapest house in the Sims 4.

### Site Goals

* To provide users with a fun quiz game to play.
* To provide users with a range of questions to test their knowledge.
* To provide users with the ability to record their scores and see how their knowledge compares to others.

### User Stories

* As a user I want a new quiz about the Sims 4 to play.
* As a user I want to be able to test my knowledge against other people.
* As a user I want to play a quiz that is unique.

### The Scope Plane

**Features planned:**
* As there are certain restrictions in the scope of the development of the application, such as the terminal confines and methods of deployment, it will be important to ensure all functionality is contained within the game terminal screen.
* Despite the confines of the terminal emulator, the site should site be visually stimulating and clear to the user that it is a game about the Sims.
* The user needs to know what their score is.
* The user should be able to record their score on a leaderboard and be able to view that leaderboard.

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
* The user should be able to play the game multiple times without having too many of the same questions repeated.  The quiz will have ten questions, but these will be randomised from a much bigger bank of questions which can easily be expanded to incorporate the possibility of new worlds in the Sims 4.

Implementation:

* The user will be able to interact with the game at other points too, such as viewing the leaderboard and the instructions.  The user will also be given multiple opportunities to exit the game.

#### Opportunities

Arising from user stories
| Opportunities | Importance | Viability / Feasibility
| ------ | :------: | :------: |
| ** Provide a fun quiz game ** | 5 | 5 |
| ** Provide a wide range of questions ** | 5 | 5 |
| ** Provide ability to record scores and compare with others ** | 5 | 5 |


### The Skeleton Plane
#### Wireframe mock-up

 I decided to centre the terminal horizontally on the screen because it feels like a nicer user experience. The run program button was centrally positioned above the terminal window to emphasise its importance.

![Home Page Wireframe](/assets/p3_wireframe_1.png)


#### Logic Flow

To begin to understand how I wanted the game to work, I prepared a couple of slides for my mentor and I in plain English.  I find it exceedingly helpful to plan in English before I start writing any code.  I used these slides to develop the logical flow of the game.

To develop the logical steps required within the game, along with gaining an understanding of how the different game elements would interact, I created a flow chart detailing the individual steps for the game.

The game logic can be broken down into three distinction sections. The initial setup of the game, answering the question and checking the result before moving on to the next question and the logic for displaying the leaderboard.  For ease of reference, I have broken up the logic flow diagram into these three sections.

The flow diagrams have been prepared in [Visio](https://www.microsoft.com/en-gb/microsoft-365/visio/flowchart-software).


##### Setup Logic

![Setup Logic](/assets/game_start.png)

##### Question Logic and Validation

![Question Logic](/assets/quiz_flow.png)

##### Leaderboard Logic

![Leaderboard Logic](/assets/write_data.png)

#### Programming Paradigm

I attempted to introduce the use of OOP (Object Oriented Programming).

I wanted to make sure that I included at least one class in the game, even though I don't fully understand the concept just yet.  I am comfortable enough using classes to build out a full application right now.  However, the application has room for expansion and refactoring.  I intend to revisit the project in the future in order to rewrite it using cleaner code blocks.

### The Surface Plane

#### Design

Given that the application will be run within a terminal emulator provided within the template, there are limited options available with regards to the layout of the webpage itself. Early on within the development of the theme, I decided that I had to find a way of doing something to give the game a recognisable Sims look. I tried to get a background image to display, but I couldn't work out how to do it and in the end I figured it wasn't that important in the scope of the project brief.  Instead we have a blue to green gradient in the background.  The blue/green is reminiscent of the Sims 4 anyway.

Aside from the background gradient, I have also styled the Play Game button and coloured it the same blue as the Sims 4 logo (#4c5c98).

I also wanted to include a favicon because I felt it would help to make the site feel polished.  I attempted to use an image for the favicon, but I could not get it to work.  I suspect this is due to the limitations of the Code Institute template, thanks to my friends on Slack for the advice on this one.  In the end, I chose to put in a web-hosted favicon from [favicon.cc](https://www.favicon.cc/?action=icon&file_id=806995).  The limitation with this is that the favicon will not display in Internet Explorer.

## Features

Please note that the game code has changed slightly since these screenshots were taken.  A few extra lines of text have been removed pertaining to asking for user input and the user now has the ability to go back to the main menu after viewing the instructions and the leaderboard.

#### Welcome Screen

![Welcome Screen](/assets/start_game.png)

At the start of game users are greeted with a welcome screen showing the game logo of a plumbob.  This is instantly recognisable to anyone who plays the Sims. The game asks the user to please enter their name.

![What do you want to do today Sreen](/assets/user_choice_first.png)

Once a user has entered their name, the next screen greets the user and asks them what they would like to do today.  The options are a) Play the game, b) View the Top Ten leaderboard, c) View the instructions, or d) Exit the game.

#### Instructions Screen

![Instructions Screen](/assets/instructions.png)

If users select the instructions option from the main menu the screen will display the objectives for the user. I've also included some Simlish translations in the instructions.  Most 'Simmers' (people who play The Sims) will be used to the little Simlish words in the game, but I appreciate that not everyone will be.

![Instructions Screen](/assets/instructions_2.png)

Users are then presented the same message as the welcome screen asking if they would like to play a game. In the finished version of the site, the user can also choose to go back to the main menu or exit the game.

#### Questions Screen

![Questions Screen](/assets/questions_1.png)

Once the user has indicated that they are ready, the first question will display.

If the user answers the question correctly, a message will be displayed informing them that they have answered correctly.

#### Incorrect Answer Screen

![Incorrect Answer Screen](/assets/questions_incorrect_answer.png)

If the user answers incorrectly, a message will be display informing them that they have answered incorrectly.

#### Invalid Answer Screen

![Invalid Answer Screen](/assets/questions_invalid_response.png)

If the user inputs anything other than a, b or c as the answer to a question, a message will be display informing them that their answer is invalid. The game will then progress to the next question.

#### End of Game Screen

![End of Game Screen](/assets/end_game.png)

The user will be asked a total of ten questions.  At the end of ten questions, a screen will be displayed informing them of their final score and how long it has taken them to answer the questions.  The user will also be asked if they would like to input their score to the leaderboard.

#### Add score to Leaderboard Screen

![Add score to Leaderboard Screen](/assets/commit_score.png)

The user will be informed that their score is being added to the Leaderboard, then they will be asked if they wish to view the leaderboard, restart the game or exit the game.

#### Leaderboard

![Leaderboard](/assets/leaderboard.png)

This screen will display the leaderboard to the user.

![Leaderboard](/assets/leaderboard_after.png)

The user will then be asked if they wish to start the game or exit the game.  In the finished version of the site, the user can also choose to go back to the main menu or exit the game.

#### Exit Game Screen

![Exit Game Screen](/assets/end_game.png)

This will thank the user for playing the game.  In the final version of the game, there is a message informing the user that they can press the blue button at the top to restart the game.

## Future Enhancements

User data - Usernames would be stored, as well as each individual's scores, so that returning users could play against themselves and try to beat their previous scores.

Further expansion of The Sims 4 - There does not seem to be a Sims 5 game coming out any time soon.  Therefore I anticipate that a few more worlds will be released in the future, meaning that my game could be expanded to incorporate these.

Further questions - At the moment there are 39 questions in the game.  I probably have enough information to write another 30 questions.  A wide variety of questions will result in less repetition of questions each time a user plays the game.


## Testing

### Testing Strategy

I took a two-stage approach to testing the application. The first stage was continuous testing as the application was being developed. With the application being based within the terminal, it was straight forward to test functions and print statements as they were being developed using the terminal within the IDE. This involved writing functions and print statements to enable me to check that the questions were being randomised correctly and that the scores were being recorded to the leaderboard correctly.

For the second stage of testing, I utilised a more formal structured approach and tested based on the earlier flow charts I had created to test the logical flows and expected outcomes of the game.

The individual python files were also validated using [pep8online.com](http://pep8online.com/), further details are below.

My Slack group (see Acknoledgements) helped me with the final debugging and made some excellent suggestions for enhancing the game, including returns to the main menu and using "Guest" as a user name if the user doesn't enter a name.


#### Validator Testing

* pep8online.com - I utilised [pep8online.com](http://pep8online.com/) to validate my python code. All python files were checked with no errors reported, other than 3 trailing white spaces which are caused by the Game Over ASCII art.  I made the decision to leave in the ASCII art because I believe it adds to the feel of the game.


* Screenshot of the validator report is here:
    * ![Screenshot of the pep8online validator tool results](/assets/pep8online.png "Screenshot of the pep8online validator tool results")


#### Notable Bugs

None as far as I know.

#### Libraries Utilised

Several python libraries were utilised to enable additional functionality within the application.

#### time
The time library was imported to utilise the time.sleep functionality. This enabled me to incorporate specific time delays within the program which adds to the player experience by simulating the time between the player's answer and the computers response. Whilst only a small time delay occurs, I felt that it was a much better experience than the computer response appearing as soon as the user has pressed their answer key. 
#### os
The os library was imported to enable me to add functionality to the terminal emulator which allowed me to clear the previous print statements. This provides a clearer and more structured experience for the user.
#### random
The random library was imported to access the built in methods of generating a random selection for the quiz questions.
#### datetime
The datetime library was imported so that I could get the date and time of when the user committed their score to the worksheet.  I thought this could be interesting in the future so that other users can see how long a high score has been there for.
#### tabulate
The tabulate library was imported so that I could exert some styling on the returned worksheet data and display it in a structured way to the user.
#### gspread
The gspread library was imported to enable reading and writing to a worksheet for the purpose of recording the high scores of users.  Gspread was also used in sorting the worksheet data so that only the top ten results are returned to the user.  I relied heavily on the [Gspread documentation](https://docs.gspread.org/_/downloads/en/v4.0.1/pdf/) in order to achieve what I needed.  I could have imported another library like Pandas, but I felt it was unnecessary.

## Deployment

The site was deployed via Heroku, and the live link can be found here - [Game](https://the-sims-4-real-estate-quiz.herokuapp.com/).

The project was developed utilising a **Code Institute** provided template.

### Project Deployment

To deploy the project through Heroku I followed these steps:
* Sign up / Log in to [Heroku](https://www.heroku.com/)
* From the main Heroku Dashboard page select 'New' and then 'Create New App'
* Give the project a name - I entered the-sims-4-real-estate-quiz and selected a suitable region, then selected create app. The name for the app must be unique.
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
* In this section, confirm the correct branch of the repo is selected in the drop-down box, and then click the Enable Automatic Deploys button if you wish to automatically deploy your site in Heroku every time you push changes to GitHub.
* My preference was to do this manually, so I chose not to Enable Automatic Deploys and I updated my Heroku app periodically.
* Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.

## Credits

### Code

I looked at several different ways of building a quiz before I embarked on the hard coding.  The method that seemed most elegant to me is well-documented on the internet, but I'm crediting this one by Brock Byrdd on [Medium](https://brockbyrdd.medium.com/creating-a-multiple-choice-quiz-in-python-terminal-1c46123b86d5).

I learnt about various ways of timing in Python from this blog article on [Udacity](https://www.udacity.com/blog/2021/09/create-a-timer-in-python-step-by-step-guide.html).

I was informed of a method to clear the terminal by reading a discussion about it on the Code Institute Slack.  The method I was using comes from a Python cheat sheet provided by [coding4you](http://www.coding4you.at/inf_tag/beginners_python_cheat_sheet.pdf).  However, my fellow student Helena Johannson (see below) pointed out that the terminal wasn't being completely cleared, so she set off looking for another method which she found on [askubuntu](https://askubuntu.com/questions/25077/how-to-really-clear-the-terminal).

I learnt about the tabulate library in this article by [Towards Data Science](https://towardsdatascience.com/how-to-easily-create-tables-in-python-2eaea447d8fd).

I learnt more about working with gspread by reading the [gspread documentation](https://docs.gspread.org/en/latest/user-guide.html).


### Content

#### Wikipedia

Wikipedia was used as a reference point for details of the Sims franchise and details of the various worlds and neighbourhoods in The Sims 4. [The Sims 4](https://en.wikipedia.org/wiki/The_Sims_4).

#### Carl's Sims 4 Guide

Carl's Sims 4 Guide has everything you could possibly need to know about The Sims 4.  I'm a big fan, but I don't know everything and again, I used it for information about the various worlds, neighbourhoods and families in The Sims 4.  [Carl's Sims 4 Guide](https://www.carls-sims-4-guide.com/).

#### Background

The gradient for the background in the html is from [Egg Gradients](https://www.eggradients.com/category/green-blue-gradient) and it is called **Valyrian Steel**.


#### Text colours in terminal

Whilst researching how to use different colours within the terminal I found Haoyi's programming blog which provided me with several ideas on how I could incorporate colours within the terminal. It can be found here [Haoyi's Programming Blog](https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html).


#### ASCII Art

The image used to make the ASCII art was downloaded from [ClipArtMax](https://www.clipartmax.com/max/m2H7d3N4K9K9b1H7/).

The program used to convert the image into ASCII art is at [Many Tools](https://manytools.org/hacker-tools/convert-images-to-ascii-art/).

The Game Over ASCII art is from [Rakko Tools](https://en.rakko.tools/tools/68/).


#### Questions

All of the questions have been written by me.


### Acknowledgements

I'd like to thank the following people:

* [Helena Johansson](https://github.com/Odden69) for coming up with a better way to clear the terminal and for unfailing support in our Slack group (see below), as well as testing my game and finding the bugs in my code.
* [Andrew Dempsey](https://github.com/andrewdempsey2018) for taking the time to play my game, look for bugs and make suggestions for further enhancements.  Your support is invaluable, as always.
* The team from Code Institute's 2021 Retro Gaming Hackathon, ["Team Noiseland"](https://hackathon.codeinstitute.net/teams/73/) (including Helena and Andrew) need mentioning because they are fantastic and I'm glad I met you all on my first two weeks of the course.  I appreciate your support so much.
* Dave Horrocks and Steven Darcy from the Portfolio 3 Slack Group.
* My mentor Adegbenga Adeye.


### Conclusion

I have had a much nicer time buidling this Python project than I did with the previous project in JavaScript. I feel eager to dive deeper into the Python world and to keep learning it.
