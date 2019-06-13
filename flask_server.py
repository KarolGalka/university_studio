from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

# Krak%C3%B3w+Krakowia
@app.route('/<placename>')
def hello_world(placename):
    placename:str = placename.replace(" ", "+")
    return 'https://www.google.pl/maps/embed/v1/place?key=AIzaSyAvRyHILWzJ8SD2_yhhoOl46504G5uTKZQ' + '&q=' + placename