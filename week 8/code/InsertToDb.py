from pymongo import MongoClient ,errors
import time,random

#url = 'mongodb+srv://fesh:f9XTsUCE5U2cT3V@cluster0.oogfs.mongodb.net/test'
url = 'mongodb+srv://joe:odunayo@cluster0.nsfju.mongodb.net/myFirstDatabase'
client = MongoClient(url)

lessons = client.lessons

inventory = lessons.inventory

inventory.drop()

fruits = ["strawberries",'bananas','apples']

for fruit in fruits:
    inventory.insert_one({"type":fruit,"quantity":100})

