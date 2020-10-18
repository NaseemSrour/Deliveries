from flask import request
from flask_restful import Resource, reqparse

from utils.errors import error_response

class Item(Resource):

    def get(self, item_id: str = None):
        """Retrives the item with the provided ID"""
        try:
            # TODO:  actual logic to be added once Database connector is available
            if (item_id is not None):
                return f"Item with ID {item_id} retrived"
            return "Item Retrieved", 200  
        except Exception as err:
            return error_response(err)

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
            return "Item Created", 201 
        except Exception as err:
            return error_response(err)

    def delete(self, item_id: str):
        """ Deletes the item with the provided ID """
        try:
            # TODO:  actual logic to be added once Database connector is available
            return "Item Created", 201 
        except Exception as err:
            return error_response(err)