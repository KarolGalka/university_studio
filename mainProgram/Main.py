import data_algorithms.nlp
import json
import databaseTest
import data_algorithms.experiments

def get_categories(result_json):
    result_categories = []
    for category in result_json['categories']:
        result_categories.append(parse_label(category['label']))
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


author_categories_set = get_fitting_tweets_categories('PaulMcCartney')
saved_categories_documents = databaseTest.read_all_categories()
saved_categories_set = get_list_from_categories_documents(saved_categories_documents)
categories_to_be_add = find_new_categories(author_categories_set, saved_categories_set)
print(categories_to_be_add)
if(len(categories_to_be_add) > 0):
    databaseTest.write_categories_to_database(categories_to_be_add)














