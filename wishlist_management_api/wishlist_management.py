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


#Create a Wishlist
@wishlist_management.route('/create_wishlist', methods = ['POST'])
def add_wishlist():
    userId = request.json['user_id']
    name = request.json['name']
    new_wishlist = Wishlist(userId=userId, name=name)
    db.session.add(new_wishlist)
    db.session.commit()
    return jsonify({'message': 'Wishlist created successfully'})

@wishlist_management.route('/add_book', methods=['POST'])
def add_book():
    wishlist_id = request.json['wishlist_id']  
    book_name = request.json['book_name']  
    # Retrieve the wishlist and book objects
    wishlist = Wishlist.query.get(wishlist_id)
    book = BookDetails.query.get(book_name)  # Assuming you have a 'BookDetails' model defined

    if wishlist and book:
        # Create a new BooksInWishlist object and associate it with the wishlist and book
        new_book_in_wishlist = BooksInWishlist(wishlistId=wishlist.id, BookId=book.id)

        db.session.add(new_book_in_wishlist)
        db.session.commit()

        return jsonify({'message': 'Book added successfully'})
    else:
        return jsonify({'message': 'Wishlist or book not found'})

#Get a wishlist
@wishlist_management.route('/get_wishlist/<int:wishlist_id>', methods=['GET'])
def get_wishlist(wishlist_id):
    wishlist = Wishlist.query.get(wishlist_id)
    
    if wishlist:
        books_in_wishlist = BooksInWishlist.query.filter_by(wishlistId=wishlist.id).all()
        
        book_list = []
        for book_in_wishlist in books_in_wishlist:
            book = BookDetails.query.get(book_in_wishlist.BookId)
            if book:
                book_data = {
                    'id': book.id,
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

#Get all wishlist 
@wishlist_management.route('/get_all_wishlist', methods = ['GET'])
def get_all_wishlist():
    all_wishlists = Wishlist.query.all()
    serialized_wishlists = [
        {'id': wishlist.id, 'userId': wishlist.userId, 'name': wishlist.name}
        for wishlist in all_wishlists
    ]
    return render_template('wishlist_list.html', wishlists=serialized_wishlists)
    
# Delete a Wishlist 
@wishlist_management.route('/delete_book/<Sing:book_name>', methods=['DELETE'])
def delete_book(book_name):
    book = BooksInWishlist.query.get(book_name)
    if book:
        db.session.delete(book)
        db.session.commit()
        return jsonify(message='Book deleted successfully')
    return jsonify(message='Book not found')
    


