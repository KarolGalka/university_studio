import data_algorithms.nlp
import json
import databaseTest
import data_algorithms.experiments

categories = "accounting airport amusement_park aquarium art_gallery atm bakery bank bar beauty_salon bicycle_store book_store bowling_alley bus_station cafe campground car_dealer car_rental " + "car_repair car_wash casino cemetery church city_hall clothing_store convenience_store courthouse dentist department_store doctor electrician electronics_store embassy fire_station " + "florist funeral_home furniture_store gas_station gym hair_care hardware_storehindu_temple home_goods_store hospital insurance_agency jewelry_store laundry lawyer library liquor_store " + "local_government_office locksmith lodging meal_delivery meal_takeaway mosque movie_rental movie_theater moving_company museum night_club painter park parking pet_store pharmacy physiotherapist plumber police post_office real_estate_agency " + "restaurant roofing_contractor rv_park school shoe_store shopping_mall spa stadium storage store subway_station supermarket synagogue taxi_stand train_station transit_station travel_agency veterinary_care zoo"

def get_categories(result_json):
    result_categories = set([])
    try:
        for category in result_json['categories']:
            result_categories.add(parse_label(category['label']))
    except Exception as e:
        print(e)
    return result_categories


def parse_label(label):
    split = label.split('/')
    return split[1]


def add_list_to_set(list, set):
    for element in list:
        set.add(element)


def get_fitting_tweets_categories(username):
    last_tweets = data_algorithms.experiments.find_user_tweets(username)
    set_of_categories = set([])
    for tweet in last_tweets:
        print(tweet.text)
        result_json = json.loads(data_algorithms.nlp.get_categories_from_text(tweet.text))
        categories = []
        try:
            categories = get_categories(result_json)
        except Exception as e:
            print(e)

        add_list_to_set(categories, set_of_categories)
    return set_of_categories


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

#  get_fitting_tweets_categories('PaulMcCartney')

def google_to_watson():
    split = categories.split(" ")
    for category in categories.split(" "):
        category = category.replace("_", " ")
        category_string = category + " " + category + " " + category + " " + category + " " + category
        result_json = json.loads(data_algorithms.nlp.get_categories_from_text(category_string))
        watson_category = get_categories(result_json)
        print("Kategoria google: " + category + "\n Kategoria watson: " + " || ".join(watson_category))


author_categories_set = google_to_watson()
# saved_categories_documents = databaseTest.read_all_categories()
# saved_categories_set = get_list_from_categories_documents(saved_categories_documents)
# categories_to_be_add = find_new_categories(author_categories_set, saved_categories_set)
# print(categories_to_be_add)
# if (len(categories_to_be_add) > 0):
#     databaseTest.write_categories_to_database(categories_to_be_add)
