from flask import Blueprint, render_template
from database import db, BookDetails

book_details = Blueprint('book_details', __name__)

@book_details.route("/book-details", methods = ['POST'] ) # api name


# sample function to create an endpoint which should return a json format

#Creates a book with it's details
def bookDetails():
    details = BookDetails.query.all()

    for book in details:
        print("Book's Title: " + book.book_name)
        print("ISBN: " + str(book.ISBN))
        print("Book's Description: " + book.book_description)
        print("Price: $" + str(book.book_price))
        print("Author: " + book.author)
        print("Genre: " + book.genre)
        print("Year of Publication: " + str(book.year_published))
        print("Copies Sold: " + str(book.copies_sold))

     #return "<h1>Hello. <br> If you see this it means your app is working. <br>This is a sample get request.  </h1>"
    return render_template("book_details_sample.html", title="sample", details=details)
