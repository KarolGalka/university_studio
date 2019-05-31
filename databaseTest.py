from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb+srv://ProjectUser:agh123@aghproject-dllxo.mongodb.net/test?retryWrites=true&w=majority")
db=client.admin
# Issue the serverStatus command and print the results
db=client.business


#
# serverStatusResult=db.command("serverStatus")
# pprint(serverStatusResult)