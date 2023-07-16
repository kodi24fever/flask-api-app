from flask import Blueprint, render_template, request
from database import db, BooksTesting, BookBrowse
import json

browse = Blueprint('browse', __name__)


def addBooksToBookBrowse():
    try:
        db.session.add(BookBrowse(title="Star Wars", author="John Ceena", rating=9, price=20.54, copies_sold=20, genre_name="Fantasy"))

        # Commit all changes to database
        db.session.commit()

    except Exception as e:
        print( f'There was an error: {str(e)}')



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

    return "This endpoint returns top sellers"



@browse.route("/browse-books-by-rating") # retrieve books by rating feature

# Return top 10 books that have sold the most copies, parameters: Rating, Response: list of books in Json Format
def getBooksByRating():

    return "This endpoint returns books by rating"



