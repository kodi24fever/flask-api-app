from flask import Blueprint, render_template
from database import db, BooksTesting

browse = Blueprint('browse', __name__)

@browse.route("/browse") # api name

# sample function to create an endpoint which should return a json format
def show_message():
    # querying the all the books using flask-sqlalchemy
    books = BooksTesting.query.all()

    # Printing all books' name
    for book in books:
        print("id: " + str(book.id))
        print("name: " + book.name)
        #print("detail: " + book.book_detail)
    return render_template("sample.html", title="sample", books=books)



@browse.route("/top-sellers") # retrieve top sellers feature

# Return top 10 books that have sold the most copies, parameters: None
def getTopSellers():

    return "This endpoint returns top sellers"



@browse.route("/books-by-rating") # retrieve books by rating feature

# Return top 10 books that have sold the most copies, parameters: Rating, Response: list of books in Json Format
def getBooksByRating():

    return "This endpoint returns books by rating"