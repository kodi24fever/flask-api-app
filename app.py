from flask import Flask
from book_browsing_sorting_api.browse import browse
from flask_sqlalchemy import SQLAlchemy
from database import db, BooksTesting, BookDetails

# Import your route file here. Remember to rename the folder to remove the number and '_' in front 
from book_details_api.book_details import book_details

# this part is the navigation bar to change between urls
app = Flask(__name__)

# databse connectionss
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database object
db.init_app(app)

# Create the .db file and tables
with app.app_context():
    # Creates non existing tables
    db.create_all()

    try:
        # Populate Fields
        populate_books = BooksTesting(id=1, name="Star Wars")

        # Create your model instance here and populate fields
        populate_books = BookDetails(book_name="The History of Jazz", ISBN="9780190087210", book_description="An updated new edition of Ted Gioia's universally acclaimed history of jazz, with a wealth of new insight on this music's past, present, and future.",
                                     book_price=24.95, author="Ted Gioia", genre="Music", year_published=2021, copies_sold=58042)


        # Add your values to the database here
        db.session.add(populate_books)




        # It commits or saves all fileds to the database
        db.session.commit()
    
    except Exception as e:
        print( f'There was an error: {str(e)}')



@app.route("/") # api name
# sample function to create an endpoint which should return a json format
def index():
    return "<h1>Hello. <br> This is index page</h1> <a href='/browse'>Browse API</a> <br><br> <a href='/profile'>Profile Managment API</a> <br><br> <a href='/shopping'>Shopping API</a> <br><br> <a href='/book-details'>Book Details API</a> <br><br> <a href='/book-rating'>Book Rating API</a>"




'''
    Below this part you can register your routes.
    This way we can have one main file that runs the entire application

'''
# Route for module 1
app.register_blueprint(browse)



'''
    Uncomment app.resister and change your file name 

'''
# Route for module 2
#app.register_blueprint(your_route)

# Route for module 3
#app.register_blueprint(your_route)

# Route for module 4
app.register_blueprint(book_details)


# Route for module 5
#app.register_blueprint(your_route)
