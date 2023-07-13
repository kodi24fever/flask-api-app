from flask import Blueprint, render_template
from database import db, BooksTesting, BookBrowse

browse = Blueprint('browse', __name__)


def addBooksToBookBrowse():
    try:
        db.session.add(BookBrowse(title="Star Wars", author="John Ceena", rating=9, price=20.54, copies_sold=20, genre_name="Fantasy"))

        # Commit all changes to database
        db.session.commit()

    except Exception as e:
        print( f'There was an error: {str(e)}')



@browse.route("/browse") # api name

# sample function to create an endpoint which should return a json format
def show_message():
    # querying the all the books using flask-sqlalchemy
    books = BookBrowse.query.all()

    # Printing all books' name
    # for book in books:
        # print("id: " + str(book.id))
        # print("name: " + book.name)
        # print("detail: " + book.book_detail)
        # db.session.delete(book)
        # print(0)
    
    # try:
    #     db.session.query(BooksTesting).delete()
    #     db.session.commit()
    # except:
    #     db.session.rollback()

    return render_template("browse.html", title="sample", books=books)



@browse.route("/browse-books-by-genre") # retrieve books by genre

# Return books by genre, parameters: Genre
def getBooksByGenre():

    return "This endpoint returns books by genre"


@browse.route("/browse-top-sellers") # retrieve top sellers feature

# Return top 10 books that have sold the most copies, parameters: None
def getTopSellers():

    return "This endpoint returns top sellers"



@browse.route("/browse-books-by-rating") # retrieve books by rating feature

# Return top 10 books that have sold the most copies, parameters: Rating, Response: list of books in Json Format
def getBooksByRating():

    return "This endpoint returns books by rating"



