from flask import Blueprint

browse = Blueprint('browse', __name__)

@browse.route("/browse") # api name


# sample function to create an endpoint which should return a json format
def show_message():
    return "<h1>Hello. <br> If you see this it means your app is working. <br>This is a sample get request.</h1>"
