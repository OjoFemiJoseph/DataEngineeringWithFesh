from pymongo import MongoClient ,errors
import time,random

#url = 'mongodb+srv://fesh:f9XTsUCE5U2cT3V@cluster0.oogfs.mongodb.net/test'
url = 'mongodb+srv://joe:odunayo@cluster0.nsfju.mongodb.net/myFirstDatabase'
client = MongoClient(url)

lessons = client.lessons

inventory = lessons.inventory


try:
    with inventory.watch(full_document='updateLookup') as change_stream_cursor:
        for data_change in change_stream_cursor:
            print(data_change)
except:
    print('change stream closed because of an error')