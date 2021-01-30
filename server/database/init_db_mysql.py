import logging

import mysql.connector
from mysql.connector import errorcode
import db_mysql_config
import db_mysql_controller

logger = logging.getLogger(__name__)


dbConfig = {
  'user': db_mysql_config.db_username,
  'password': db_mysql_config.db_password,
  'host': db_mysql_config.db_host,
  'database': db_mysql_config.db_name, 'autocommit':True
}


# Create DB if it doesn't exist
initial_db_config = {
  'user': db_mysql_config.db_username,
  'password': db_mysql_config.db_password,
  'host': db_mysql_config.db_host, 'autocommit':True
}

mydb = mysql.connector.connect(**initial_db_config)
mycursor = mydb.cursor()
isExist = False
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    if x == db_mysql_config.db_name:
      logger.info("Database '" + db_mysql_config.db_name + "' already exists")
      isExist = True

if (isExist == False):
    logger.info("Database '" + db_mysql_config.db_name + "' doesn't exit, creating it..")
    mycursor.execute("CREATE DATABASE " + db_mysql_config.db_name)

mycursor.close()
mydb.close()



# Create tables
logger.info("Creating tables...")
db = mysql.connector.connect(**dbConfig)
cursor = db.cursor()


for line in open(db_mysql_config.create_all_tables_path):
    cursor = db_mysql_controller.execute_query(cursor, query=line)
    
logger.info("Tables created succesfully!")
cursor.close()
db.close()