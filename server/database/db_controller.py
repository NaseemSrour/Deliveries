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
