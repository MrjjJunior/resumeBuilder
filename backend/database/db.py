import pymongo as pm

client = pm.MongoClient("mongodb://localhost:27017/")

# print(client)

database = client["DataBase"]
column  = database["user"]

user_info = {"name": "Tshepsio", "email" : "tlhongtshepiso2@gmail.com"}

insert = column.insert_one(user_info)

print(client.list_database_names())

