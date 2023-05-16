# Welcome to flask-api-app!


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


### Happy Coding!