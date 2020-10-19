import mysql.connector
from mysql.connector import errorcode
import config
import db_controller

dbConfig = {
  'user': config.db_username,
  'password': config.db_password,
  'host': config.db_host,
  'database': config.db_name, 'autocommit':True
}


db = mysql.connector.connect(**dbConfig)
cursor = db.cursor()


for line in open(config.create_all_tables_path):
    cursor = db_controller.execute_query(cursor, query=line)
    

cursor.close()
db.close()
