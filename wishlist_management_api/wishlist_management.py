from flask import Flask, request, jsonify
from flask import Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
from database import db, Wishlist
# from flask_marshmallow import Marshmallow
import os


wishlist_management = Blueprint('wishlist_management', __name__)
current_dir = os.path.dirname(os.path.abspath(__file__))


# ma = Marshmallow(wishlist_management)

# ProductSchema class
class ProductSchema():
    class Meta:
        fields = ('id', 'userId', 'name')

#Innit Schema
# product_schema = ProductSchema()


#Create a Wishlist
@wishlist_management.route('/wishlist', methods = ['POST'])
def add_wishlist():
    userId = request.json['user_id']
    name = request.json['name']
    new_wishlist = Wishlist(userId=userId, name=name)
    db.session.add(new_wishlist)
    db.session.commit()
    return jsonify({'message': 'Wishlist created successfully'})

#Get all wishlist 
@wishlist_management.route('/get_all_wishlist', methods = ['GET'])
def get_wishlist():
    all_wishlists = Wishlist.query.all()
    serialized_wishlists = [
        {'id': wishlist.id, 'userId': wishlist.userId, 'name': wishlist.name}
        for wishlist in all_wishlists
    ]
    return render_template('wishlist_list.html', wishlists=serialized_wishlists)
    

# Delete a Wishlist (example route, needs modification)
@wishlist_management.route('/delete_wishlist/<int:wishlist_id>', methods=['DELETE'])
def delete_wishlist(wishlist_id):
    wishlist = Wishlist.query.get(wishlist_id)
    if wishlist:
        db.session.delete(wishlist)
        db.session.commit()
        return jsonify(message='Wishlist deleted successfully')
    return jsonify(message='Wishlist not found')
    


