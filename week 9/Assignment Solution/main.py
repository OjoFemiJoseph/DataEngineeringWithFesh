from pymongo import MongoClient ,errors
from datetime import datetime
from pandas import json_normalize
import pymysql

run_datetime = datetime.now()

def connectdb():
    
    conn =pymysql.connect(
        user = 'root',
        password = '',
        db = 'test',
        host = 'localhost',
    )
    print("success in connecting", conn)
    return conn
    
def mongo_connect():
    url = ''
    client = MongoClient(url)

    lessons = client.lessons

    inventory = lessons.inventory.find({})
    
    return inventory

def save_to_parquet(inventory,run_datetime):
    df = json_normalize(list(inventory))
    df.to_parquet(f"{str(run_datetime).replace(':',' ')}.gzip",
              compression='gzip')
    return df

def save_to_csv(inventory,run_datetime):
    
    df = json_normalize(list(inventory))
    df.to_csv(f"{str(run_datetime).replace(':',' ')}.csv")

    return df
    

try:
    conn = connectdb()
    #db = sqlite3.connect('week_eight.db')
    cur = conn.cursor()

    cur.execute("""
            CREATE TABLE IF NOT EXISTS `week_eight` (
                    `run_time` varchar(255) ,
                    `total_runtime` varchar(255) ,
                    `document_count` varchar(255) ,
                    `success_status` varchar(255) 
                    );

                """)

    

    try:
        inventory = mongo_connect()
        df = save_to_csv(inventory,run_datetime)
        document_count = df.shape[0]
        success_status = 'True'
    except:
        document_count = 0
        success_status = 'False'

    total_time_to_run = str(datetime.now() - run_datetime )

    #print(run_datetime,'-',document_count,'-',success_status,total_time_to_run)
    run_datetime = run_datetime.strftime("%Y-%m-%d %H:%M:%S")
    query = f"INSERT INTO week_eight VALUES ('{run_datetime}','{total_time_to_run}',{document_count},'{success_status}')"
    print(query)
    cur.execute(query)
    conn.commit()
    conn.close()
    print('inserted')

except:
    total_time_to_run = str(datetime.now() - run_datetime )
    #print(run_datetime,'-',document_count,'-',success_status,total_time_to_run)
    run_datetime = run_datetime.strftime("%Y-%m-%d %H:%M:%S")
    document_count = 0
    success_status = 'False'
    query = f"INSERT INTO week_eight VALUES ('{run_datetime}','{total_time_to_run}',{document_count},'{success_status}')"
    
    with open('error.txt','a+') as file:
        file.write(query)
        file.write('\n')
        
