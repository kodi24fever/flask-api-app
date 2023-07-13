from flask import Blueprint, render_template, request, jsonify
from database import db, BookDetails



book_details = Blueprint('book_details', __name__)


class ProductSchema():
    class Meta:
        details = ('book_name', 'ISBN', 'book_description', 'book_price',
                   'author', 'genre', 'year_published', 'copies_sold')


product_schema = ProductSchema()

@book_details.route("/book_details", methods=['POST']) # api name


# sample function to create an endpoint which should return a json format
# Creates book with it's details
def add_book_Details():
    book_name = request.json['book_name']
    ISBN = request.json['ISBN']
    book_description = request.json['book_description']
    book_price = request.json['book_price']
    author = request.json['author']
    genre = request.json['genre']
    year_published = request.json['year_published']
    copies_sold = request.json['copies_sold']

    new_book_Details = BookDetails(
            book_name = book_name,
            ISBN = ISBN,
            book_description = book_description,
            book_price = book_price,
            author = author,
            genre = genre,
            year_published = year_published,
            copies_sold = copies_sold
    )

    db.session.add(new_book_Details)
    db.session.commit()

    return jsonify({'message': 'Book details added successfully'})

@book_details.route("/search_by_ISBN/<ISBN>", methods=['GET'])
def get_details_ISBN(ISBN):
    find_by_ISBN = BookDetails.query.filter_by(ISBN = ISBN).all()
    if find_by_ISBN:
        serialized_book_details = [
            {
              'book_name': add_book_Details.book_name,
              'ISBN': add_book_Details.ISBN,
              'book_description': add_book_Details.book_description,
              'book_price': add_book_Details.book_price,
              'author': add_book_Details.author,
              'genre': add_book_Details.genre,
              'year_published': add_book_Details.year_published,
              'copies_sold': add_book_Details.copies_sold
            }

            for add_book_Details in find_by_ISBN

        ]

        return render_template('details.html', get_details_ISBN= serialized_book_details)

    else:
        return jsonify(message = 'No book was found with this ISBN')






    #details = BookDetails.query.all()

    #for book in details:
        #print("Book's Title: " + book.book_name)
        #print("ISBN: " + str(book.ISBN))
        #print("Book's Description: " + book.book_description)
        #print("Price: $" + str(book.book_price))
        #print("Author: " + book.author)
        #print("Genre: " + book.genre)
        #print("Year of Publication: " + str(book.year_published))
        #print("Copies Sold: " + str(book.copies_sold))





     #return render_template("book_details_sample.html", title="sample", details=details)
