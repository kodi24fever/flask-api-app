from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Model for Feature 1: Book Sorting (sample)
class BooksTesting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

'''
    Below here you can create the model or table for the database.
    The python class is your model name.
    db.Model is an argument required bu SQLAlchemy
    Inside the class you specify he fields.
    All is done using Flask-SQLAlchemy[https://flask-sqlalchemy.palletsprojects.com/en/2.x/]
    Databse is SQLite
'''


# Database Model for Feature 2:

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


# Database Model for Feature 5:

# Databse Model for Feature 6:
