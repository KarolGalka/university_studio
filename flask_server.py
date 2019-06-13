from flask import Flask
from flask_cors import CORS
import os
from .orchestrator import get_places

print(os.getcwd())
app = Flask(__name__)
CORS(app)

# Krak%C3%B3w+Krakowia
@app.route('/')
def hello_world():#placename):
    places = get_places()
    print("PLACES: ", places)
    placename = places[0]
    placename:str = placename.replace(" ", "+")
    return 'https://www.google.pl/maps/embed/v1/place?key=AIzaSyAvRyHILWzJ8SD2_yhhoOl46504G5uTKZQ' + '&q=' + placename