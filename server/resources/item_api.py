import os
import sys
import json
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
print(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
import logging 

from flask_restful import Resource, reqparse

from utils.errors import error_response
import database.db_controller as db_controller
import models.db_entities.db_item as db_item

logger = logging.getLogger(__name__)


def dictify_DBItem(my_item):
    item_dict = {}
    item_dict["item_id"] = my_item.ID
    item_dict["item_name"] = my_item.name
    item_dict["item_desc"] = my_item.desc
    # NEED TO FIGURE OUT HOW TO RETURN AN IMAGE. Cannot put bytes in a json (which is called 'serialization')
    # item_dict["image"] = my_item.image
    item_dict["price"] = my_item.price
    item_dict["business_id"] = my_item.business_id
    return item_dict

class ItemAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('item_id', type = int, required = True, help = {"The requested item's ID number"})
        super(ItemAPI, self).__init__()


    
    def get(self, item_id=None):
        """Retrives the item with the provided ID"""
        try:
            logger.info("Server's GET item request")
            if (item_id is not None):
                retrieved_item = db_item.get_item(item_id)
                
                if retrieved_item is None:
                    return {"error": "Item with ID " + str(item_id) + " was not found!"}, 404
                
                item_dict = dictify_DBItem(retrieved_item)
                item_json = json.dumps(item_dict)
                response = item_dict, 200
                return response
            
        except Exception as err:
            logger.error(str(err))
            return {"error": str(err)}

    def post(self):
        """Created a new item"""
        try:
            # TODO:  actual logic to be added once Database connector is available
            return "Item Created", 201 
        except Exception as err:
            return error_response(err)

    def put(self, item_id: str):
        """ Updates the Item with the provided ID """
        try:
            # TODO:  actual logic to be added once Database connector is available
            return "Item Created", 200 
        except Exception as err:
            return error_response(err)

    def delete(self, item_id: str):
        """ Deletes the item with the provided ID """
        try:
            # TODO:  actual logic to be added once Database connector is available
            return "Item Created", 200 
        except Exception as err:
            return error_response(err)
