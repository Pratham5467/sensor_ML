
from pymongo.mongo_client import MongoClient
import pandas as pd
import json


uri = "mongodb+srv://srivastavapratham52:srivastavapratham52@cluster0.qj0ivgu.mongodb.net/?retryWrites=true&w=majority"

DATABASE_NAME="pwskills"
COLLECTION_NAME="waferfault"
# Create a new client and connect to the server
client = MongoClient(uri)

df=pd.read_csv("C:\Users\Pratham srivastava\OneDrive - Sikkim Manipal University\Desktop\sensor_proj\notebooks\wafer_23012020_041211.csv")
df=df.drop("Unnamed: 0",axis=1)
json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)