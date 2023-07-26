from flask import Flask
from flask import Blueprint, render_template, request, jsonify
from database import db, User, CreditCard
import json
from werkzeug.security import generate_password_hash, check_password_hash

profile = Blueprint('profile', __name__)

@profile.route("/profile", methods=['GET'])
def userDetails():
    users = User.query.all()

    for user in users:
        print("Username: " + user.username)
        print("Password: " + user.password)
        print("Name: " + user.name)
        print("Email: " + user.email)
        print("Home Address: " + user.home_address)

    return render_template("user_details.html", title="User Details", users=users)

@profile.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'],
                    password=hashed_password,
                    name=data['name'],
                    email=data['email'],
                    home_address=data['home_address'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'New user created!'}), 201

@profile.route('/user/<username>', methods=['GET'])
def get_user(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'message': 'User not found!'}), 404

    user_data = {'username': user.username,
                 'name': user.name,
                 'email': user.email,
                 'home_address': user.home_address}
    return jsonify(user_data), 200

@profile.route('/update_user', methods=['PUT'])
def update_user():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if not user:
        return jsonify({'message': 'User not found!'}), 404

    if 'password' in data:
        if not check_password_hash(user.password, data['password']):
            return jsonify({'message': 'Invalid password!'}), 403

    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    user.home_address = data.get('home_address', user.home_address)
    db.session.commit()
    return jsonify({'message': 'User updated!'}), 200

@profile.route('/create_credit_card', methods=['POST'])
def create_credit_card():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if not user:
        return jsonify({'message': 'User not found!'}), 404

    new_card = CreditCard(user_id=user.id, card_number=data['card_number'],
                          cardholder_name=data['cardholder_name'],
                          expiration_date=data['expiration_date'])
    db.session.add(new_card)
    db.session.commit()
    return jsonify({'message': 'New card created!'}), 201

