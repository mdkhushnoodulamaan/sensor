from pymongo.mongo_client import MongoClient
import pandas as pd
import json

# uniform resource identifier
uri = "mongodb://Amaan:Amaan123@ac-pswyy9o-shard-00-00.o6nab3s.mongodb.net:27017,ac-pswyy9o-shard-00-01.o6nab3s.mongodb.net:27017,ac-pswyy9o-shard-00-02.o6nab3s.mongodb.net:27017/?ssl=true&replicaSet=atlas-vgbrkb-shard-0&authSource=admin&retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# create database name and collection name 
DATABASE_NAME="pwskills"
COLLECTION_NAME="waferfault"

# read the data as as dataframe
df = pd.read_csv(r"E:\ML project\Walter Fault_copy\notebooks\wafer_23012020_041211.csv")
df=df.drop("Unnamed: 0",axis=1)

# Convert the data into json
json_record = list(json.loads(df.T.to_json()).values())

# now dump the data into the database
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)