from flask import Blueprint, request, render_template
from database import db, BookBrowse, BookRatingComment, UserProfile
from datetime import datetime

book_rating = Blueprint('book_rating', __name__)


@book_rating.route("/book-rating", methods=['GET', 'POST'])
def book_details_by_id():
    # Retrieve book_id from the GET request or default to 8
    book_id = request.args.get('book_id', default=8, type=int)

    book = BookBrowse.query.get(book_id)

    if not book:
        return "Book not found", 404

    if request.method == 'POST':
        user_id = request.form.get('user_id')
        if not user_id:
            return "Username is required to submit comments.", 400

        comment = request.form.get('comment')
        rating = request.form.get('rating')

        new_entry = BookRatingComment(
            book_name=book.title,
            user_id=user_id,
            rating=rating if rating else None,
            comment=comment if comment else None,
            timestamp=datetime.now()
        )
        db.session.add(new_entry)
        db.session.commit()

    # Calculate average rating
    avg_rating = db.session.query(db.func.avg(BookRatingComment.rating)) \
        .join(BookBrowse, BookBrowse.title == BookRatingComment.book_name) \
        .filter(BookBrowse.id == book.id).scalar()

    # Retrieve all comments
    comments = BookRatingComment.query.filter_by(book_name=book.title).all()

    return render_template("book-rating.html", book=book, avg_rating=avg_rating, comments=comments)
