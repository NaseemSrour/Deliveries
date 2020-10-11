import mysql.connector
from mysql.connector import errorcode
import json

dbConfig = {
  'user': 'root',
  'password': 'sqlninja678',
  'host': 'localhost',
  'database': 'delivery', 'autocommit':True
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
    
'''
q = input("enter query: ")
db = mysql.connector.connect(**dbConfig)
cursor = db.cursor()
cursor = execute_query(q, cursor)
if(cursor is not None):
    for x in cursor:
        print(x)
    cursor.close()
db.close()
'''


# NEXT IS BUILDING THE INSERT AND FETCHING QUERIES
def add_item(item):
    # data = (item['item_name'], item['item_desc'], "load_file('" + item['image_path'] + "')", item['price'], item['business_id'])
    item = json.loads(item)
    insert_item_query = "INSERT INTO Item(item_name, item_desc, image, price, business_id) VALUES('{}', '{}', {}, '{}', '{}');".format(item["item_name"], item["item_desc"], "load_file('" + item["image_path"] + "')", item["price"], item["business_id"])
    ## insert_item_query = "INSERT INTO Item(item_name, item_desc, image, price, business_id) VALUES('{}', '{}', {}, '{}', '{}');".format(item[0],
                                                                                                                            ## item[1], "load_file('" + item[2] + "')", item[3], item[4])


    '''
    values = "VALUES('" + item{'item_name'} + "', "
    values = values + "'" + item{'item_desc'} "', "
    values = values + "load_file('" + item.image_path + "'), "
    values = values + item{'price'} + ", " + item{'business_id'} + ")"
    query = query + values + ";"
    '''
    
    db = mysql.connector.connect(**dbConfig)
    cursor = db.cursor()
    cursor = execute_query(cursor, insert_item_query)
    cursor.close()
    db.close()

    return "Success"

'''
#Example new item:
my_new_item = {}
my_new_item['item_name'] = 'Steak 5nzer'
my_new_item['item_desc'] = 'Steak 5nzer bnaqi6'
my_new_item['image_path'] = 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/steak_5nzer.jpg'
my_new_item['price']= 33
my_new_item['business_id'] = 1

add_item(my_new_item)
'''
