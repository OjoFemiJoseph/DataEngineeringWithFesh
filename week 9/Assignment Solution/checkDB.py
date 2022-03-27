from pymongo import MongoClient ,errors
from datetime import datetime
from pandas import json_normalize
import sqlite3

db = sqlite3.connect('week_eight.db')
cur = db.cursor()


cur.execute('SELECT * FROM week_eight')
print(cur.fetchone())