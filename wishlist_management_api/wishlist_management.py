from flask import Flask, request, jsonify
from flask import Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
from database import db, Wishlist, BooksInWishlist, BookDetails
import os


wishlist_management = Blueprint('wishlist_management', __name__)
current_dir = os.path.dirname(os.path.abspath(__file__))

# ProductSchema class
class ProductSchema():
    class Meta:
        fields = ('id', 'userId', 'name')
        
#Innit Schema
product_schema = ProductSchema()


#Create a Wishlist [DONE]
@wishlist_management.route('/create_wishlist', methods = ['POST'])
def add_wishlist():
    userId = request.json['user_id']
    name = request.json['name']
    existing_wishlists_count = Wishlist.query.filter_by(userId=userId).count()
    #Check if the number of wishlist the user has is equal or less than 3 
    if existing_wishlists_count >= 3:
        return jsonify({'message': 'User already has 3 wishlists. Cannot create more. Sorry :('}), 403

    new_wishlist = Wishlist(userId=userId, name=name)
    db.session.add(new_wishlist)
    db.session.commit()
    return jsonify({'message': 'Wishlist created successfully'})

#Add book to wishlist [DONE]
@wishlist_management.route('/add_book', methods=['POST'])
def add_book():
    wishlist_id = request.json['wishlist_id']  
    book_name = request.json['book_name']  
    
    # Retrieve the wishlist and book objects
    wishlist = Wishlist.query.get(wishlist_id)
    book = BookDetails.query.filter_by(book_name=book_name).first()

    if wishlist and book:
        # Check if the book is already in the wishlist
        existing_book = BooksInWishlist.query.filter_by(wishlistId=wishlist.id, book_name=book_name).first()
        if existing_book:
            return jsonify({'message': 'Book already exists in the wishlist'}), 403
        
        # Create a new BooksInWishlist object and associate it with the wishlist and book
        new_book_in_wishlist = BooksInWishlist(wishlistId=wishlist.id, book_name=book.book_name)

        db.session.add(new_book_in_wishlist)
        db.session.commit()

        return jsonify({'message': 'Book added successfully'})
    else:
        return jsonify({'message': 'Wishlist or book not found'})

#Get books from a wishlist [DONE]
@wishlist_management.route('/get_wishlist/<int:wishlist_id>', methods=['GET'])
def get_wishlist(wishlist_id):
    wishlist = Wishlist.query.get(wishlist_id)
    
    if wishlist:
        books_in_wishlist = BooksInWishlist.query.filter_by(wishlistId=wishlist.id).all()
        
        book_list = []
        for book_in_wishlist in books_in_wishlist:
            book = BookDetails.query.get(book_in_wishlist.book_name)
            if book:
                book_data = {
                    'book_name': book.book_name,
                    'ISBN': book.ISBN,
                    'book_description': book.book_description,
                    'book_price': book.book_price,
                    'author': book.author,
                    'genre': book.genre,
                    'year_published': book.year_published,
                    'copies_sold': book.copies_sold
                }
                book_list.append(book_data)
        
        return jsonify({'books': book_list})
    else:
        return jsonify({'message': 'Wishlist not found'})
    
# Delete a book [DONE]
@wishlist_management.route('/delete_book', methods=['DELETE'])
def delete_book():
    wishlistId = request.json['wishlist_id']  
    book_name = request.json['book_name']  
    
    wishlist = Wishlist.query.get(wishlistId)

    if wishlist is None:
        return jsonify(message='Wishlist not found')
    
    book = BooksInWishlist.query.filter_by(wishlistId=wishlist.id, book_name=book_name).first()
    if book is None:
        return jsonify(message='Book not found')   
    db.session.delete(book)
    db.session.commit()
    return jsonify(message='Book deleted successfully')
    
    

