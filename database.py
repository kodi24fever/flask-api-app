from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Model for Feature 1: Book Sorting (sample)
class BooksTesting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))


# Database Model for Feature 2:

# Databse Model for Feature 3:

# Databse Model for Feature 4:

# Database Model for Feature 5:

# Databse Model for Feature 6: