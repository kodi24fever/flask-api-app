from flask import Flask
from book_browsing_sorting_api.browse import browse

# Import your route file here. Remember to rename the folder to remove the number and '_' in front 


# this part is the navigation bar to change between urls
app = Flask(__name__)
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
#app.register_blueprint(your_route)

# Route for module 5
#app.register_blueprint(your_route)