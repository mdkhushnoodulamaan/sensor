import os


AWS_S3_BUCKET_NAME = "wafer-fault"
MONGO_DATABASE_NAME = 'pwskills'
MONGO_COLLECTION_NAME = 'waferfault'

TARGET_COLUMN = 'quality'
MOGNO_DB_URL = "mongodb://Amaan:Amaan123@ac-pswyy9o-shard-00-00.o6nab3s.mongodb.net:27017,ac-pswyy9o-shard-00-01.o6nab3s.mongodb.net:27017,ac-pswyy9o-shard-00-02.o6nab3s.mongodb.net:27017/?ssl=true&replicaSet=atlas-vgbrkb-shard-0&authSource=admin&retryWrites=true&w=majority"

MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION = ".pkl"

artifact_folder = "artifacts"