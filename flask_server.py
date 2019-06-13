from flask import Flask
from flask_cors import CORS
from flask import render_template
import os
from .orchestrator import get_places

print(os.getcwd())
app = Flask(__name__)
CORS(app)

# Krak%C3%B3w+Krakowia
@app.route('/')
def main_page():
    return render_template('localization.html')


@app.route('/<nickname>')
def hello_world(nickname):
    places = get_places(nickname)
    print("PLACES: ", places)
    placename = places[0]
    placename:str = placename.replace(" ", "+")
    return 'https://www.google.pl/maps/embed/v1/place?key=AIzaSyAvRyHILWzJ8SD2_yhhoOl46504G5uTKZQ' + '&q=' + placename