from flask import Flask
from flask import Blueprint, render_template
from database import db, UserProfile

profile = Blueprint('profile', __name__)

@profile.route("/profile", methods=['GET']) # api name

# sample function to create an endpoint which should return a json format
def userDetails():
    users = UserProfile.query.all()

    for user in users:
        print("Username: " + user.username)
        print("Password: " + user.password)
        print("Name: " + user.name)
        print("Email: " + user.email)
        print("Home Address: " + user.home_address)

    return render_template("user_details.html", title="User Details", users=users)
    #return "<h1>Hello. <br> If you see this it means your app is working. <br>This is a sample get request.  </h1>"