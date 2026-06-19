import pymongo as pm

client = pm.MongoClient("mongodb://localhost:3000/")

# print(client)

database = client["DataBase"]



print(client.list_database_names())

