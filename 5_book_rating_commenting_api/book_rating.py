from flask import Flask

app = Flask(__name__)

@app.route("/book-rating") # api name


# sample function to create an endpoint which should return a json format
def bookRating():
    return "<h1>Hello. <br> If you see this it means your app is working. <br>This is a sample get request.  </h1>"