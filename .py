import pymongo
import pandas as pd
import sklearn
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC
df=pd.read_csv("New Institutes - New Institutes.csv")
from pymongo import MongoClient
client=pymongo.MongoClient("mongodb://localhost/mongodb-27017")
database=client.db["DataBase1"]
collection=client.subdatabase
df
def insert_data():
    collection.insert_many(df)
    return sid
insert_data()
def count_Data():
    a=collection.find_many({},{"State":"Andhra Pradesh"})
    list.append(a)
    print(a)
