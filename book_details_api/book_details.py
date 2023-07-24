from flask import Blueprint, render_template, request, jsonify
from database import db, BookDetails, AuthorDetails



book_details = Blueprint('book_details', __name__)




@book_details.route("/admin/create_book_details", methods=['POST']) # api name
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

        return render_template('ISBN_details.html', get_details_ISBN= serialized_book_details)

    else:
        return jsonify(message = 'No book was found with this ISBN')



@book_details.route("/admin/create_author", methods=['POST'])
def create_author():


    author_fn = request.json['author_fn']
    author_ln = request.json['author_ln']
    biography = request.json['biography']
    publisher = request.json['publisher']


    new_author = AuthorDetails(

        author_fn = author_fn,
        author_ln = author_ln,
        biography = biography,
        publisher = publisher,

    )

    db.session.add(new_author)
    db.session.commit()

    return jsonify({'message': 'New Author created successfully'})


@book_details.route("/search_by_author/<author>", methods=['GET'])
def get_details_author(author):
    search_author = BookDetails.query.filter_by(author = author).all()
    if search_author:

        authors_book_details = [
            {


                'book_name': add_book_Details.book_name,

            }
            for add_book_Details in search_author

        ]

        return render_template('author_details.html', get_details_author=authors_book_details)

    else:
        return jsonify(message='No book was found for this author')



