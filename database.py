from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate # adding migrate

db = SQLAlchemy()
migrate = Migrate() # Initializes migrate object


# Model for Feature 1: Book Sorting (sample)
class BooksTesting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    book_detail = db.Column(db.String(50))

# Model for Feature 1: Book Sorting (production)
class BookBrowse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(50))
    rating = db.Column(db.Integer)
    price = db.Column(db.Float)
    copies_sold = db.Column(db.Integer)
    genre_name = db.Column(db.String(50))


class BookBrowseGenre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre_name = db.Column(db.String(50))


'''
    Below here you can create the model or table for the database.
    The python class is your model name.
    db.Model is an argument required bu SQLAlchemy
    Inside the class you specify he fields.
    All is done using Flask-SQLAlchemy[https://flask-sqlalchemy.palletsprojects.com/en/2.x/]
    Databse is SQLite
'''


# Database Model for Feature 2:
class UserProfile(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String)
    home_address = db.Column(db.String)
# Databse Model for Feature 3:

# Databse Model for Feature 4:
class BookDetails(db.Model):
    book_name = db.Column(db.String, primary_key=True)
    ISBN = db.Column(db.Integer)
    book_description = db.Column(db.String)
    book_price = db.Column(db.Float)
    author = db.Column(db.String)
    genre = db.Column(db.String)
    year_published = db.Column(db.Integer)
    copies_sold = db.Column(db.Integer)

class AuthorDetails(db.Model):
    author_fn = db.Column(db.String, primary_key=True)
    author_ln = db.Column(db.String)
    biography = db.Column(db.String)
    publisher = db.Column(db.String)


# Database Model for Feature 5:
class BookRatingComment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String)
    user_id = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    comment = db.Column(db.String)


# Databse Model for Feature 6:
class Wishlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    name = db.Column(db.String)

class BooksInWishlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wishlistId = db.Column(db.Integer)
    BookId = db.Column(db.Integer)
