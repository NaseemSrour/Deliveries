import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import mysql.connector
from mysql.connector import errorcode
import json
import config

# print(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

dbConfig = {
  'user': config.db_username,
  'password': config.db_password,
  'host': config.db_host,
  'database': config.db_name, 'autocommit':True
}


def execute_query(query, data=None):
    db = mysql.connector.connect(**dbConfig)
    cursor = db.cursor()
    try:
        cursor.execute(query, data) # Data can be None in: execute(op, data=None)
        print("query: " + query + " with data: " + str(data))
        print("executed successfully!")
        # fetchall() returns a list of tuples:
        results = cursor.fetchall() # Results can be None
        cursor.close()
        db.close()
        return results
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist!")
        else:
            print("Executing query " + query + " failed: {}".format(err))

        if(cursor is not None):
            cursor.close()
        if(db is not None):
            db.close()

        return None
