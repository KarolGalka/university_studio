from flask import Flask
from flask_cors import CORS
from flask import render_template
import json
import os
import time
from flask import Response
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

    if(len(places) == 0):
        return Response(status=404)

    # print("PLACES: ", places)
    # places = [{'entity': 'Muzeum Narodowe w Krakowie', 'category': 'art and entertainment'}, {'entity': 'Maxi Moda Kraków', 'category': 'style and fashion'}, {'entity': 'Ogród Zoologiczny w Krakowie', 'category': 'pets'}]
    places_json = json.dumps(places)
    print(places_json)

    # if(places)



    # time.sleep(1)
    return places_json