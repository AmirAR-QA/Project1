# Core Project

## Contents
* [Brief](https://github.com/AmirAR-QA/Project1#brief)
   * [Listed Requirements](https://github.com/AmirAR-QA/Project1#listed-project-requirements)
   * [Created With](https://github.com/AmirAR-QA/Project1#created-with)
* [Layout](https://github.com/AmirAR-QA/Project1#layout)
* [Architecture](https://github.com/AmirAR-QA/Project1#architecture)
   * [Database Relationship Diagram](https://github.com/AmirAR-QA/Project1#database-relationship-diagram)
   * [CI Pipeline](https://github.com/AmirAR-QA/Project1#ci-pipeline)
* [Project Management](https://github.com/AmirAR-QA/Project1#project-management)
* [Risk Assessment](https://github.com/AmirAR-QA/Project1#risk-assessment)
* [Testing](https://github.com/AmirAR-QA/Project1#testing)
* [Application](https://github.com/AmirAR-QA/Project1#application)
* [Future Development](https://github.com/AmirAR-QA/Project1#future-development)
* [Contributors](https://github.com/AmirAR-QA/Project1#contributors)
* [Acknowledgments](https://github.com/AmirAR-QA/Project1#acknowledgements)
* [Licensing](https://github.com/AmirAR-QA/Project1#licensing)

## Brief 

I have been tasked with creating a basic CRUD app, this app Creates, Reads, Updates, and Deletes data. This will showcase my knowledge and understanding of the programs that we've discussed so far. 

## Listed Project Requirements

* A Trello board with  user stories, use cases and tasks needed to complete the project and risks/problems encountered. 
* A relational database this database needs to have at least 2 tables in it with an ERD.
* Clear Documentation from a design phase describing the architecture you will use for you project as well as a detailed Risk Assessment.
* A functional CRUD application created in Python
* Fully designed test suites for the application you are creating as well as automated tests for validation of the application.
* A functioning front-end website and integrated API's, using Flask.
* Code fully integrated into a Version Control System using the Feature-Branch model which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.

## Created With

* Visual Studio Code - IDE
* GCP - Database and instance host
* MySQL - Database language
* Jenkins - CI pipeline
* Git - Version control
* GitHub - Repository and version control
* Trello - Project management
* Pytest - Unit testing
* Selenium - Integration testing
* Draw.io - ERD creation

## Layout

To satisfy the requirements of this project I created an app with allows users to create players, and items for a fantasy game and assign the items to a player. In more detail:

* Create a player that has the following attributes:
   * *Player name*
   * *Player class*
   * *Level*

* Create an item that can be assigned to a player, the item has the following attributes:
   * *Item name* of the post
   * *Value (in gold pieces)*
   * *Weight (in kg)*
   * *Rarity*

* The user can take an item and assign it to any player, and can easily delete or update any of the fields above for their character.
* When the user first starts up the app, the app presents a list of all the items currently in the database displayed alongside the played they've been assigned to.

## Architecture

### Database Relationship Diagram

![ERD](https://i.imgur.com/URk9NDA.png)

Displayed above is my Entity Relationship Diagram and the intial scope of my project. As indicated by the key, the red boxes are features which were not yet implemented and the green features are features which are complete and functioning. 

The relationship between the Players and Items tables are a "One to Many" relationship as one Player may hold multiple Items. This satisfies the relational aspect of the project.

### CI Pipeline

![CI](https://i.imgur.com/PcgtRtR.png)

The pipeline displayed above was my working stream. 
* Worked out what to work on first and tracked all streams of work with my Trello board
* I started by developing the code of the app using Python and flask
* Pushed the code to this GitHub repository
* Cloned the repository into my GCP instance
* Pulled the code, built and ran the app via Jenkins
* Tested the code with Pytest (unit testing) and Selenium (integration testing)
* I accordingly adjusted my code till it passed my assertions and pushed to my GitHub to be rebuilt by Jenkins
* I then used Jenkins to build the final app for presentation

I had intended to run the testing via jenkins itself but the skills required are, as of yet, not in my grasp. 

## Project Management

The Trello board I used to track and manage tasks while developing the app can be found here (https://trello.com/b/Co65bKUV/qa-project-1). 

I archived lists as I went and moved cards from left to right, going from it's conception as a User Story to the Design, and Testing lists (now archived) and then to the Doing and Completed lists (still visible) 

![TB](https://i.imgur.com/Qq0qtZ4.png)

The User Stories that have been entered come with Acceptance Criteria in the comments, like so;

![US](https://i.imgur.com/NvCXOFm.png)

## Risk Assessment

![RA](https://i.imgur.com/uH8FiIy.png)

The following matrix shows my risk assessments. The first three risks I forsaw during my intial planning stage. Later on I realised, I had included in older commits my Secret Key to the database. Perhaps other secure pieces of information were available in older commits. I added risk 4 after this. Similarly, I added risk 5 when I had an outage during development and realised that GCP may be prone to outages too. 

## Testing

Testing was carried out in 2 main ways via selenium which was integration testing, and pytest which was unit testing. My selenium testing is still very basic only really covered the most basic app functions which satisfied the CRUD functionality expected by the project brief. My unit testing was more developed, with a total coverage of 90%. There were a few stray lines here and there that I didn't know how to test and there were two sections in my routes.py file which I tried to create a test for but wasn't successful. That's a point for continual development.

## Application

My application is fully functional and has no bugs (that I've yet found). The following is a breakdown of how it works:

![image1](https://i.imgur.com/tSdog8C.png)

On the additems or addplayers page you add an item or player along with the required values. Each value is necassary and not inputing one of them will return a prompt to fill in the blanks. 

![image2](https://i.imgur.com/fl83J2q.png)

On the items or players page the item or player is displayed in a table form, from where you can delete or update the record. 

![image3](https://i.imgur.com/VC2jcUb.png)

Updating an item will allow you to assign it to a player. This is an example of the updateitems screen.

![image4](https://i.imgur.com/gNxDzjV.png)

The home page displays the owner of each item by pulling the player name via the id in the items table. Once you successfully update an item you will be redirected to this screen. 


## Future Development

There are a few points of improvements I'd like to carry out. 

* The first is storing secret keys and any confidential data in a virtual environment using getenv when necassary.
* I'd like to be able to add more tables to assign items
* I'd like to further develop my Selenium testing
* I'd like to test my update fields with unit testing

All of the above have not already been completed because of a severe lack of development time and an unforseenly large about of time troubleshooting otherwise trivial issues (like the 2 hours I spent hunting down a stray comma).

One point of improvement I'd like to implement would be the creation of an functionality which allows you to log in with a user so that all your players and items are saved for each user rather than on the database at large. This wasn't something required or part of my scope at the start of the project.

A note on versioning - The current app is fully functional and without any major (or percievable minor) bugs. Thus the version number is 0.1.0.


## Contributors

Me, Amir. 

## Acknowledgements

Nick, Ben, and Raji for providing me with the relevant skills needed to be able to code the app. 

## Licensing 

MIT License

Copyright (c) [2021] [Amir Abdur-Rahman]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
