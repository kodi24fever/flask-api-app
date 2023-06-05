from flask import Blueprint
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
    return "<h1>Hello. <br> If you see this it means your app is working. <br>This is a sample get request.</h1>"
