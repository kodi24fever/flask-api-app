from flask import Flask
from flask import Blueprint, render_template, request, jsonify
from database import db, UserProfile, User
import json

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

@profile.route("/create_user", methods=['POST'])
def create_user():
    data = request.json  # Assuming the request data is in JSON format
    username = data['username']
    password = data['password']
    name = data.get('name')
    email = data.get('email')
    home_address = data.get('home_address')

    # Create a new User instance and add it to the database
    new_user = User(username=username, password=password, name=name, email=email, home_address=home_address)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201
