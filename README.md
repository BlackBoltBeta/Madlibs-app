#  Llama Mad Libs

This is a simple app to play Mad Libs with. It welcomes the user with a straightforward message on how to play and then presents the user with several themes to choose from. It is intended for children as a simple pastime.

![Responsive Mockup](assets/images/responsive-screens.png)

## User Goals 

 - To get amused with a silly text for a short period of time.


## Features 

### Existing Features

- __Welcome message__

  - This section shows what  themes the user can choose from and what he needs to input to access them.

![dice-select]

- __Themes__

 - Currently, there are three options available to play with: 
   - Instructions for the babysitter
   - Going to the doctor
   - Bats are so cool.

![giant dice]

- __Different Madlibs__

  - After being asked for a few different words, the user will be presented with a filled-out Mad Libs to read out loud.

![Theme change]

## Design diagram 

- __Project Requirements__

 - Python application using libraries/API and deployed to a cloud-based platform.
 - The code itself, just like the game, it is very simple:
   - A function to present the user with a choice of themes. 
   - A separate function for each Madlibs. These consist of a group of inputs to fill out a template literal.
   - A boolean if statement to protect the input from non-alphabetical characters.

![giant dice]

### Things to improve:

- At the moment,  every madlib is a separate function. So grouping them  and the word selections into an array might help to make the code less verbose.


## Technologies and libraries used

__Main languages__

- __Python__
-  __HTML:__ Provided in the Code Institute template
-  __CSS:__ Provided in the Code Institute template
-  __JavaScript:__ Provided in the Code Institute template

__Python libraries and api used__

-  Termcolor

## Testing 

- Testing has been conducted continuously during the development process. Manual testing has been conducted by the author.

### Validator Testing 

  - No errors were found. The code has been tested by using PEP8 CI Python Linter https://pep8ci.herokuapp.com/#

## Development and Deployment
 
- The development environment used for this project was GitPod. To track the development stage and handle version control regular commits and pushes to GitHub has been conducted. The GitPod environment was created using a template provided by Code Institute.

The live version of the project is deployed using Heroku(https://heroku.com)

This is how this project was deployed using Heroku:

To prepare for deployment on Heroku a requirements.txt needs to be created in the same folder as the .py file in GitPod. This file needs to contain a list of all libraries the project needs to run as a Heroku App.

Then follow these steps:

Login to Heroku (Create an account if necessary)
Click on New in the Heroku dashboard and select ”Create new app”
Write a name for the app and choose your region and click ”Create App”
In the settings tab for the new application I created two Config vars.
One is named CREDS and contains the credentials key for Google Drive API
One is name PORT and has the value of 8000
Two buildpack scripts were added: Python and Nodejs (in that order)
Heroku CLI was used to deploy the project. The following steps were taken in the terminal in GitPod

Deploying your app to heroku

Login to heroku and enter your details.
command: heroku login -i
Get your app name from heroku.
command: heroku apps
Set the heroku remote. (Replace app_name with your actual app name)
command: heroku git:remote -a app_name
Add, commit and push to github
command: git add . && git commit -m "Deploy to Heroku via CLI"
Push to both github and heroku
command: git push origin main
command: git push heroku main
After those steps were taken the application was deployed at the following link: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

## Credits 

Resources and tutorials used for developing this project:
- Templates and ideas taken from [Wordlibs](https://www.thewordfinder.com/wordlibs/)
-  Inspiration came from this childrens book [Llama Llama Mad Libs Junior: World's Greatest Word Game](https://www.amazon.com/Llama-Mad-Libs-Junior/dp/1524790346)
- Colors used from the library: [termcolor ](https://pypi.org/project/termcolor/#description)

Massive thanks to, [Lauren-Nicole Popich](https://www.linkedin.com/in/lauren-nicole-popich-1ab87539/) my Code Institute mentor, for her guidance.
