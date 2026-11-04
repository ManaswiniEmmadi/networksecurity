from pymongo import MongoClient
uri = "mongodb+srv://emmadimanaswini17_db_user:<pasword>@cluster0.wjtafdc.mongodb.net/"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)