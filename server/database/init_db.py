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


# Create DB if it doesn't exist
initial_db_config = {
  'user': config.db_username,
  'password': config.db_password,
  'host': config.db_host, 'autocommit':True
}

mydb = mysql.connector.connect(**initial_db_config)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    if x == config.db_name:
      print("Database '" + config.db_name +"' already exists"
    else:
        print("Database '" + config.db_name +"' doesn't exit, creating it..")
        mycursor.execute("CREATE DATABASE " + config.db_name)

mycursor.close()
mydb.close()



# Create tables
print("Creating tables...")
db = mysql.connector.connect(**dbConfig)
cursor = db.cursor()


for line in open(config.create_all_tables_path):
    cursor = db_controller.execute_query(cursor, query=line)
    
print("Tables created succesfully!")
cursor.close()
db.close()
