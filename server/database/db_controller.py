import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import mysql.connector
from mysql.connector import errorcode
import json
import config


dbConfig = {
  'user': config.db_username,
  'password': config.db_password,
  'host': config.db_host,
  'database': config.db_name, 'autocommit':True
}

def execute_query(cursor, query, data=None):
    try:
        if(data is None):
            cursor.execute(query)
            print("query: " + query)
            print("executed successfully")
            return cursor
        else:
            cursor.execute(query, data)
            return cursor
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist!")
        else:
            print("Executing query " + query + " failed: {}".format(err))
        return None


def get_item(item_id):
    select_query = "SELECT item_name, item_desc, price, business_id FROM Item WHERE item_id=" + item_id + ";"
    db = mysql.connector.connect(**dbConfig)
    cursor = db.cursor()
    cursor = execute_query(cursor, select_query)
    row = cursor.fetchone()
    if(row is not None):
        cursor.close()
        db.close()
        # Suggestion: Use here the DBItem class to create an object and save the data (row) in it, and then return this object instead of returning 'row' as a tuple.
        return row
    else:
        return("Item with ID " + item_id + " + is not found!")


    
def add_item(item):
    item = json.loads(item)
    insert_item_query = "INSERT INTO Item(item_name, item_desc, image, price, business_id) VALUES('{}', '{}', {}, '{}', '{}');".format(item["item_name"], item["item_desc"], "load_file('" + item["image_path"] + "')", item["price"], item["business_id"])
    
    db = mysql.connector.connect(**dbConfig)
    cursor = db.cursor()
    cursor = execute_query(cursor, insert_item_query)
    cursor.close()
    db.close()

    return "Success"
