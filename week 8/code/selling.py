from pymongo import MongoClient ,errors
import time,random

#url = 'mongodb+srv://fesh:f9XTsUCE5U2cT3V@cluster0.oogfs.mongodb.net/test'
url = 'mongodb+srv://joe:odunayo@cluster0.nsfju.mongodb.net/myFirstDatabase'
client = MongoClient(url)

lessons = client.lessons

inventory = lessons.inventory


fruits = ["strawberries",'bananas','apples']
quantities = [-1,-2,-4,-3]

while True:
    random_fruit = random.choice(fruits)
    random_quantity = random.choice(quantities)
    inventory.update_one({"type":random_fruit,"quantity":{"$gt":10}},{"$inc":{"quantity":random_quantity}})
    time.sleep(1)