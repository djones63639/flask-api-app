# Welcome to flask-api-app!

## 	How it Works
Our flask-api-app is an web based application that contains different API's (Application Programming Interfaces) routes that connects to a database and and users, or developers, are able to see the data from the database.

- First, the application contains navigation links to a respective feature.
- Each feature contains its owns logic.
- database.py functions as database models.
- app.py is the main file that runs the entire application, and also for populating basic dummy data.
- Populating data can be done using flask shell, in this case, we used a try-except clauses to catch the error in case data is repeated, so the app does not stop running.

## 	Required Software
`python >= 3.10.x` [Download](https://www.python.org/downloads/)

Any text editorL
 - [Visual Studio Code](https://code.visualstudio.com/download)
 - [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows)

 
## Installation

 1. [Download](https://www.python.org/downloads/) and Install python. 
 2. Fork this repository and Clone it from your account. [Check here](https://docs.github.com/en/get-started/quickstart/fork-a-repo) on how to fork. [Check Here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) on how to clone a repository.
 3. `cd flask-api-app` and enter root directory of the application.

## How to Install .env folder

 1. Inside root folder. Run `py -m venv .venv` for Windows or `python3 -m venv .venv` for Mac or Linux, to create a .env folder environment.
 2. Activate environment `.\.venv\Scripts\activate`. You should see something like this 
`(.venv) PS C:\Users\defaultUser\Desktop\flask-api-app>` on your terminal.
 3. Once environment is activated you can install the requirements including flask `pip install -r requirements.txt`

## How to run the app
The app contains 5 folder for each rest api.

 1. Change directory to your respective rest api folder or create a new one.
 2. Run `flask --app .\your_file.py run --debug` and start editing the file.
 3. Go to `localhost:5000/your-endpoint-name` and you should see a welcome message.


## How to correctly run the app
The app contains app.py file that works as a navigation bar where you can change to url.

 1. Change directory to root directory.
 2. Run `flask --app app.py run --debug` and start editing your file.
 3. Go to `localhost:5000` and you should see a welcome message and links to your porject url.
 4. Click your project link button or go to `localhost:5000/your-endpoint-name` and you should see a welcome message.


# Important Note related to adding your files to app.py
1. Remember to make the required changes using [flask blueprint](https://flask.palletsprojects.com/en/2.2.x/blueprints/).
2. Check the book_browsing_sorting_api as a guide.
3. Remember to register your route in app.py.


### Happy Coding!