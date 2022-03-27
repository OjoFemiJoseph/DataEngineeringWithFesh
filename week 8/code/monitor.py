from pymongo import MongoClient ,errors
import time,random

#url = 'mongodb+srv://fesh:f9XTsUCE5U2cT3V@cluster0.oogfs.mongodb.net/test'
url = 'mongodb+srv://joe:odunayo@cluster0.nsfju.mongodb.net/myFirstDatabase'
client = MongoClient(url)

lessons = client.lessons

inventory = lessons.inventory


low_quantity_pipeline = [{"$match":{"fullDocument.quantity":{"$lt":20}}}]

try:
    with inventory.watch(pipeline=low_quantity_pipeline, full_document="updateLookup") as change_stream_cursor:
        for data_change in change_stream_cursor:
            current_quantity = data_change["fullDocument"].get("quantity")
            fruit = data_change["fullDocument"].get("type")
            msg = "There are only {0} units left of {1}".format(current_quantity,fruit)
            print(msg)
except errors.PyMongoError:
    logging.error("change stream closed because of an error")