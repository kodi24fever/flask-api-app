from flask import Blueprint, render_template, request, redirect
from database import db, BooksTesting, BookBrowse
import json
import random

browse = Blueprint('browse', __name__)


@browse.route("/browse") # api name
# index reqquest for browse feature
def index():
    return render_template("browse.html", title="Browse and Sorting API")


@browse.route("/browse-books-by-genre") # retrieve books by genre
# Return books by genre, parameters: Genre
def getBooksByGenre():

    # Get parameters from template
    genre = request.args.get('genre')

    # Query BookBrowse
    books = BookBrowse.query.filter_by(genre_name=genre).all()

    jsonBooks = []

    if books:
        for book in books:
            
            if book:
                jsonBooks.append({
                    'id': book.id,
                    'title': book.title,
                    'author': book.author,
                    'rating': book.rating,
                    'price': book.price,
                    'copies_sold': book.copies_sold,
                    'genre_name': book.genre_name
                })

        return render_template("browse_books_by_genre.html", title="Browse By Genre", books = json.dumps(jsonBooks))
                
    else:
        

        return render_template("browse_books_by_genre.html", title="Browse By Genre", books = json.dumps({'books': 'There is no data to show'}))



@browse.route("/browse-top-sellers") # retrieve top sellers feature
# Return top 10 books that have sold the most copies, parameters: None
def getTopSellers():

    topSellers = BookBrowse.query.order_by(BookBrowse.copies_sold.desc()).limit(10).all()

    jsonTopSellers = []

    if topSellers:

        for topSeller in topSellers:

                jsonTopSellers.append({
                    'id': topSeller.id,
                    'title': topSeller.title,
                    'author': topSeller.author,
                    'rating': topSeller.rating,
                    'price': topSeller.price,
                    'copies_sold': topSeller.copies_sold,
                    'genre_name': topSeller.genre_name
                })

        return render_template("browse_top_sellers.html", title="Browse 10 Top Sellers", books = json.dumps(jsonTopSellers))
                
    else:
        return render_template("browse_top_sellers.html", title="Browse 10 Top Sellers", books = json.dumps({'topSellers': 'There is no data to show'}))



@browse.route("/browse-books-by-rating") # retrieve books by rating feature
# Return books with a particular rating or higher, parameters: Rating, Response: list of books in Json Format
def getBooksByRating():

    user_rating = request.args.get('rating')

    booksByRating = BookBrowse.query.filter(BookBrowse.rating >= int(user_rating)).order_by(BookBrowse.rating).all()

    jsonBooksByRating = []

    if booksByRating:
        for book in booksByRating:
                jsonBooksByRating.append({
                    'id': book.id,
                    'title': book.title,
                    'author': book.author,
                    'rating': book.rating,
                    'price': book.price,
                    'copies_sold': book.copies_sold,
                    'genre_name': book.genre_name
                })

        return render_template("browse_by_rating.html", title="Browse By Rating", books = json.dumps(jsonBooksByRating))
                
    else:
        return render_template("browse_by_rating.html", title="Browse By Rating", books = json.dumps({'booksByRating': 'There are no books with that rating or higher'}))






# Functions separated to the features
def addBooksToBookBrowse():
    try:
        db.session.add(BookBrowse(title="Mad Max", author="Tom Hardy", rating=5, price=11.54, copies_sold=random(1, 1000), genre_name="Action"))
        db.session.add(BookBrowse(title="The Black House", author="Stephen King", rating=5, price=25.54, copies_sold=random(1, 1000), genre_name="Horror"))
        db.session.add(BookBrowse(title="Another Day", author="Leonel Squirrel", rating=1, price=22.30, copies_sold=random(1, 1000), genre_name="Fantasy"))

        # Commit all changes to database
        db.session.commit()

        return ''


    except Exception as e:
        print( f'There was an error: {str(e)}')

        return ''
    

# def deleteBooks():
#     db.session.query(BookBrowse).delete()
#     db.session.commit()
#     return ''