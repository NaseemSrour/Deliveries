import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))  # import 'server' folder
import database.db_controller as db_controller

class DBItem:
    def __init__(self, itemName: str, itemDesc: str, img: bytes, price: int, business_id: int, itemID: int = None):
        self.ID = itemID  # auto-generated inside the DB.
        self.name = itemName
        self.desc = itemDesc
        self.image = img
        self.price = price
        self.business_id = business_id

    ##### MISSING: BLOBs handling (the 'image' column)
    def add_item(self):
        insert_item_query = "INSERT INTO Item(item_name, item_desc, price, business_id) VALUES(%s, %s, %s, %s)"
        data = (self.name, self.desc, self.price, self.business_id)

        result = db_controller.execute_query(insert_item_query, data)  # 'result' should be equal to None on success.
        print("Item " + self.name + " added successfully.")

    ##### Missing: BLOBs handling (the 'image' column)
    def update_item(self):
        update_query = "UPDATE item SET item_name=%s, item_desc=%s, price=%s WHERE item_id=%s AND business_id=%s"
        data = (self.name, self.desc, self.price, self.ID, self.business_id)
        db_controller.execute_query(update_query, data)  # returns None

    def delete_item(self):
        delete_statement = "DELETE FROM item WHERE item_id=%s AND business_id=%s"
        data = (self.ID, self.business_id)
        db_controller.execute_query(delete_statement, data)  # Returns None
        
    
    def __str__(self):
        return str([self.ID, self.name, self.desc, self.price, self.business_id])


##### Missing: BLOBs handling
# Returns: DBItem instance, or None on failure.
def get_item(item_id: int) -> DBItem:
    if(type(item_id) != int):  # MAYBE WE ALSO PREVENT USER FROM INPUTING ANYTHING OTHER THAN A NUMBER (in the  web forms + in the HTTP requests).
        return("item_id must be int!")
    
    select_query = "SELECT item_id, item_name, item_desc, price, business_id FROM Item WHERE item_id=%s"  # This way is called binding params, which is a safe way to prevent a SQL injection attack - because MySQL makes sure the value is of the correct type.
    data = (item_id,) # a comma endicates a Tuple
    results = db_controller.execute_query(select_query, data) # Returns a list of tuples; in this case, should be one tuple.
    
    if(results is not None and len(results) > 0):
        res_item = results[0]
        if(res_item[0] != item_id):
            return("Item with ID " + str(item_id) + " was not found!")
        
        retrieved_item = DBItem(res_item[0], res_item[1], res_item[2], None, res_item[3], res_item[4]) # Indexes are according to the SELECT statement above.
        return retrieved_item
    
    else:
        return("Item with ID " + str(item_id) + " was not found!")


##### MISSING: BLOBs handling
# Returns: list of DBItem instances, or None at failure.
def get_items(businessID: int) -> list[DBItem]:
    if(type(businessID) != int):
        return("business_id must be int!")
    select_query = "SELECT item_name, item_desc, price, business_id FROM item WHERE item.business_id=%s"
    data = (businessID,)
    results = db_controller.execute_query(select_query, data)  # returns a list of tuples

    db_items_lst = []
    if(results is not None and len(results) > 0):
        for row in results:
            retrieved_item = DBItem(row[0], row[1], None, row[2], row[3])
            db_items_lst.append(retrieved_item)
        return db_items_lst
    else:
        print("No items in business with ID " + str(businessID))
        return db_items_lst  # We can eliminate the if-else and just always return db_items_lst, but for now I want to keep the print statement when the above IF condition fails.


def test():
    new_item = DBItem("lafe kbeere", "lafet 5nzeer kbere'3", None, 25, 1)
    print(new_item.name + "'s price is: " + str(new_item.price) + ", it contains: " + new_item.desc)
    new_item.add_item()

# call here these functions to actually view/edit data in the DB.

'''
aa = DBItem("aaa", "aa", None, 100, 1)
#print(aa)
my_items = get_items(1)
for item in my_items:
    print(item)
'''


