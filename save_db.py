import json
import pymongo
import pandas as pd


def save_data():
    df1 = pd.read_json('data.json')

    connection = pymongo.MongoClient('localhost', 27017)
    database = connection['bdprojet']
    collection = database['données']

    records = json.loads(df1.T.to_json()).values()
    collection.insert_many(records)


def load_data():
    connection = pymongo.MongoClient('localhost', 27017)
    database = connection['bdprojet']
    collection = database['données']
    cursor = collection.find()
    entries = list(cursor)
    df = pd.DataFrame(entries)
    return df
