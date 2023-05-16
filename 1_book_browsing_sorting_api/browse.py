from flask import Flask

app = Flask(__name__)

@app.route("/browse") # api name


# sample function to create an endpoint which should return a json format
def profile():
    return "<h1>Hello. <br> If you see this it means your app is working. <br>This is a sample get request.</h1>"