from flask import Blueprint, request, jsonify
from database import db, BookRatingComment

book_rating = Blueprint('book_rating', __name__)

@book_rating.route("/book_rating", methods=['POST']) # API route
def add_book_rating_comment():
    book_name = request.json['book_name']
    user_id = request.json['user_id']
    rating = request.json['rating']
    comment = request.json['comment']

    new_book_rating_comment = BookRatingComment(
        book_name=book_name,
        user_id=user_id,
        rating=rating,
        comment=comment,
    )

    db.session.add(new_book_rating_comment)
    db.session.commit()

    return jsonify({'message': 'Book rating and comment added successfully'})

@book_rating.route("/book_rating/<book_name>", methods=['GET'])
def get_book_rating_comments(book_name):
    book_rating_comments = BookRatingComment.query.filter_by(book_name=book_name).all()

    serialized_book_rating_comments = [
        {
            'id': book_rating_comment.id,
            'user_id': book_rating_comment.user_id,
            'rating': book_rating_comment.rating,
            'comment': book_rating_comment.comment,
        }
        for book_rating_comment in book_rating_comments
    ]

    return jsonify(serialized_book_rating_comments)
