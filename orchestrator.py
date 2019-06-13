from .data_algorithms import nlp
import json
from . import databaseTest
from .data_algorithms import twitter_functions
from .frontend import simple_gui as gui
from .resources.places import PLACES_DICT
#categories = "accounting airport amusement_park aquarium art_gallery atm bakery bank bar beauty_salon bicycle_store book_store bowling_alley bus_station cafe campground car_dealer car_rental " + "car_repair car_wash casino cemetery church city_hall clothing_store convenience_store courthouse dentist department_store doctor electrician electronics_store embassy fire_station " + "florist funeral_home furniture_store gas_station gym hair_care hardware_storehindu_temple home_goods_store hospital insurance_agency jewelry_store laundry lawyer library liquor_store " + "local_government_office locksmith lodging meal_delivery meal_takeaway mosque movie_rental movie_theater moving_company museum night_club painter park parking pet_store pharmacy physiotherapist plumber police post_office real_estate_agency " + "restaurant roofing_contractor rv_park school shoe_store shopping_mall spa stadium storage store subway_station supermarket synagogue taxi_stand train_station transit_station travel_agency veterinary_care zoo"


def get_best_categories(all_categories):
    categories_dict = {}
    for entry in all_categories:
        for category in entry["categories"]:
            power_of_category = (category["score"] - 0.3) * entry["signs"]
            main_category = category["label"].split("/")[1]
            if not categories_dict.get(main_category):
                categories_dict[main_category] = {"power_of_category": 0}
            categories_dict[main_category]["power_of_category"] += power_of_category
    sorted_categories = sorted(categories_dict.items(), key=lambda x: x[1]["power_of_category"], reverse=True)
    best_categories = {category[0] for i, category in enumerate(sorted_categories) if i < 3}
    return best_categories


def parse_label(label):
    split = label.split('/')
    return split[1]


def get_fitting_tweets_categories(username):
    last_tweets = twitter_functions.find_user_tweets(username)
    all_categories = list()
    for tweet in last_tweets:
        if not twitter_functions.is_tweet_valuable(tweet):
            continue
        result_json = nlp._get_categories_from_text(tweet.text)
        if result_json:
            all_categories.append(result_json)
    return get_best_categories(all_categories)


def get_all_saved_categories():
    categories_list = []
    categories_documents = databaseTest.read_all_categories()
    for document in categories_documents:
        categories_list.append(document['name'])
    return categories_list


def find_new_categories(retrieved_categories, stored_categories):
    return stored_categories.symmetric_difference(retrieved_categories)
    # for retrieved_category in retrieved_categories:
    #     if(stored_categories.contains(retrieved_category)):
    #         categories_to_add.append(retrieved_category)
    # return categories_to_add


def get_list_from_categories_documents(categories_document):
    category_list = set([])
    for document in categories_document:
        category_list.add(document['name'])
    return category_list


#

def get_categories_from_json():
    with open('./resources/places.json') as json_file:
        data = json.load()
        return data

# def google_to_watson():
#     split = categories.split(" ")
#     for category in categories.split(" "):
#         category = category.replace("_", " ")
#         category_string = category + " " + category + " " + category + " " + category + " " + category
#         result_json = json.loads(data_algorithms.nlp.get_categories_from_text(category_string))
#         watson_category = get_categories(result_json)
#         print("Kategoria google: " + category + "\n Kategoria watson: " + " || ".join(watson_category))
def get_places(username):
    # username = gui.get_username()
    author_categories: set = get_fitting_tweets_categories(username)
    places = [PLACES_DICT[category] for category in author_categories]
    return places
    # gui.show_proposals(username, places, author_categories)
# check username


# saved_categories_documents = databaseTest.read_all_categories()
# saved_categories: set = get_list_from_categories_documents(saved_categories_documents)
# categories_to_be_add = find_new_categories(author_categories, saved_categories)
# print(categories_to_be_add)
# if (len(categories_to_be_add) > 0):
#     databaseTest.write_categories_to_database(categories_to_be_add)
