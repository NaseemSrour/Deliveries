import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import logging 

import mysql.connector
from mysql.connector import errorcode
import json
import db_mysql_config

logger = logging.getLogger(__name__)

# print(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

dbConfig = {
  'user': db_mysql_config.db_username,
  'password': db_mysql_config.db_password,
  'host': db_mysql_config.db_host,
  'database': db_mysql_config.db_name, 'autocommit':True
}


def execute_query(query: str, data: tuple=None):
    db = mysql.connector.connect(**dbConfig)
    cursor = db.cursor()
    try:
        cursor.execute(query, data) # Data can be None in: execute(op, data=None)
        logger.info("query: " + query + " with data: " + str(data))
        logger.info("executed successfully!")
        if(query.startswith("SELECT") == True):
            # fetchall() returns a list of tuples:
            results = cursor.fetchall() # Results can be None
            cursor.close()
            db.close()
            return results
        else:
            cursor.close()
            db.close()
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            logger.error("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            logger.error("Database does not exist!")
        else:
            logger.error("db_controller: Executing query " + query + " failed: {}".format(err))

        if(cursor is not None):
            cursor.close()
        if(db is not None):
            db.close()

        return None
