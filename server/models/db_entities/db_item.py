from logging import error
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))  # import 'server' folder

import logging

import database.db_controller as db_controller
import utils.binary_file_ops as file_ops
from marshmallow import Schema, fields, post_load

logger = logging.getLogger(__name__)


class DBItemSchema(Schema):
        ID = fields.Integer(allow_none=True)
        name = fields.Str()
        desc = fields.Str()
        image = fields.Str(allow_none=True) ############ For now
        price = fields.Integer()
        business_id = fields.Integer()


        @post_load
        def make_db_item(self, data, **kwargs):
            return DBItem(**data)


class DBItem():

    schema = DBItemSchema()
    
    def __init__(self, name: str, desc: str, image: bytes, price: int, business_id: int, ID: int = None):
        self.ID = ID  # auto-generated inside the DB.
        self.name = name
        self.desc = desc
        self.image = image
        self.price = price
        self.business_id = business_id


    def add_item(self):
        insert_item_query = "INSERT INTO Item(item_name, item_desc, image, price, business_id) VALUES(%s, %s, %s, %s, %s)"
        data = (self.name, self.desc, self.image, self.price, self.business_id)

        result = db_controller.execute_query(insert_item_query, data)  # 'result' should be equal to None on success.
        logger.info("Item " + self.name + " added successfully.")


    def update_item(self):
        update_query = "UPDATE item SET item_name=%s, item_desc=%s, image=%s, price=%s WHERE item_id=%s AND business_id=%s"
        data = (self.name, self.desc, self.image, self.price, self.ID, self.business_id)
        db_controller.execute_query(update_query, data)  # returns None


    def delete_item(self):
        delete_statement = "DELETE FROM item WHERE item_id=%s AND business_id=%s"
        data = (self.ID, self.business_id)
        db_controller.execute_query(delete_statement, data)  # Returns None
        
    def toJson(self):
        return(DBItem.schema.dumps(self))

    @classmethod
    def toObject(cls, jsoned_item):
        return(cls.schema.loads(jsoned_item))
    
    def __str__(self):
        # Print without the image bytes.
        return str([self.ID, self.name, self.desc, self.price, self.business_id])

    def __repr__(self):
        # Print without the image bytes.
        return f"<DBItem(name='{self.name}', desc='{self.desc}', price='{self.price}')>"



# Returns: DBItem instance, or None on failure.
def get_item(item_id: int) -> DBItem:
    if(type(item_id) != int):  # MAYBE WE ALSO PREVENT USER FROM INPUTING ANYTHING OTHER THAN A NUMBER (in the  web forms + in the HTTP requests).
        err_msg = "item_id must be int!"
        logger.error(err_msg)
        return(None)
    
    select_query = "SELECT item_id, item_name, item_desc, image, price, business_id FROM Item WHERE item_id=%s"  # This way is called binding params, which is a safe way to prevent a SQL injection attack - because MySQL makes sure the value is of the correct type.
    data = (item_id,) # a comma endicates a Tuple
    results = db_controller.execute_query(select_query, data) # Returns a list of tuples; in this case, should be one tuple.
    
    if(results is not None and len(results) > 0):
        res_item = results[0]
        if(res_item[0] != item_id):
            err_msg = "Item with ID " + str(item_id) + " was not found!"
            logger.error(err_msg)
            return(None)
        
        retrieved_item = DBItem(res_item[1], res_item[2], res_item[3], res_item[4], res_item[5], res_item[0]) # Indexes are according to the SELECT statement above.
        return retrieved_item
    
    else:
        err_msg = "Item with ID " + str(item_id) + " was not found!"
        logger.error(err_msg)
        return(None)


# Returns: list of DBItem instances, or None at failure.
def get_items(businessID: int) -> list[DBItem]:
    if(type(businessID) != int):
        err_msg = "business_id must be int!"
        logger.error(err_msg)
        return (err_msg)
    select_query = "SELECT item_id, item_name, item_desc, image, price, business_id FROM item WHERE item.business_id=%s"
    data = (businessID,)
    results = db_controller.execute_query(select_query, data)  # returns a list of tuples

    db_items_lst = []
    if(results is not None and len(results) > 0):
        for row in results:
            retrieved_item = DBItem(row[1], row[2], row[3], row[4], row[5], row[0])
            db_items_lst.append(retrieved_item)
        return db_items_lst
    else:
        logger.error("No items in business with ID " + str(businessID))
        return db_items_lst  # We can eliminate the if-else and just always return db_items_lst, but for now I want to keep the print statement when the above IF condition fails.


# ---------------------------

# Local stam tests:

def test_serialize_item():

    new_item = DBItem("sala6a", "Tabouli", None, 32, 1)
    my_json = new_item.toJson()
    print("my json: " + my_json)
    new_dbitem = DBItem.toObject(my_json)
    print(repr(new_dbitem))
    print(new_dbitem.toJson())

def test_add_item():
    myimgdata = file_ops.convertToBinaryData('C:\\Users\\Naseem\\Desktop\\Untitled.png')

    new_item = DBItem("sala6a", "Tabouli", myimgdata, 32, 1)
    print(new_item.name + "'s price is: " + str(new_item.price) + ", it contains: " + new_item.desc)
    new_item.add_item()

def test_get_item(item_id):
    salad = get_item(item_id)

    file_ops.writeBinaryFile('C:\\Users\\Naseem\\Desktop\\sala6a.png', salad.image)

def test_update_item(item_id):
    baguette = get_item(item_id)
    baguette.desc = baguette.desc + " + 3ejel mix"
    baguette.update_item()

def test_get_items(business_id):
    mylist = get_items(business_id)
    for item in mylist:
        print(item)

# call here these functions to actually view/edit data in the DB.

test_serialize_item()

