from pymongo import MongoClient


MONGO_DB_URL = "mongodb+srv://ProjectUser:agh123@aghproject-dllxo.mongodb.net/test?retryWrites=true&w=majority"

def find_all_tweets(author):
    client = MongoClient(MONGO_DB_URL)
    db = client.agency
    return db.tweet.find({'author': author})

def write_to_database(entity):
    client = MongoClient(MONGO_DB_URL)
    db = client.agency
    db.tweet.insert_one(entity)


def read_all_categories():
    client = MongoClient(MONGO_DB_URL)
    db = client.categories
    return db.tweet.find()

def write_categories_to_database(category_names):
    client = MongoClient(MONGO_DB_URL)
    db = client.categories
    for name in category_names:
        # entity = {'name' : category_name}
        # print(entity)
        # print(category_names[entity])
        entity = {'name' : category_names[name], 'category' : name}
        db.tweet.insert_one(entity)


# tweets_string = json.dump("")
#
#
# result=db.reviews.insert_one(tweet)


# serverStatusResult=db.command("serverStatus")
# pprint(serverStatusResult)


# with open('./resources/tweets.json') as json_file:
#     data = json.load(json_file)
#     for p in data['tweets']:
#         split = p.split(" ")
#         i = 0
#         for word in split:
#             if(re.match("https.*",word)):
#                 del split[i]
#             i = i +1
#         tweet = ' '.join(split)
#         entity = {
#             'author' : 'sample',
#             'tweet' : tweet
#         }
#         print(entity)
#         db.tweet.insert_one(entity)