import sys
sys.path.append('C:\\Users\\Naseem\\Desktop\\Deliveries\\')

from flask import request
from flask_restful import Resource, reqparse
# from utils.errors import error_response
from models.db_entities.db_item import DBItem
from database import db_controller

class Item(Resource):
    def get(self, item_id=None):
        """Retrives the item with the provided ID"""
        try:
            # TODO:  actual logic to be added once Database connector is available
            if (item_id is not None):
                retrieved_item = db_controller.get_item(item_id)
                return retrieved_item
                # Further to-do: handling a successful response properly in Flask Restful
            return "Item Retrieved", 200  
        except Exception as err:
            return str(err)

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
