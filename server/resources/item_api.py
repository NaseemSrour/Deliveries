import os
import sys
import json

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
print(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
import logging

from flask_restful import Resource, reqparse
from flask import request

from utils.errors import error_response
# import database.db_mysql_controller as db_mysql_controller
import models.db_entities.db_item as db_item

logger = logging.getLogger(__name__)


def dictify_DBItem(my_item):
    item_dict = {}
    item_dict["item_id"] = my_item.ID
    item_dict["item_name"] = my_item.name
    item_dict["item_desc"] = my_item.desc
    ###################### NEED TO FIGURE OUT HOW TO RETURN AN IMAGE. Cannot put bytes in a json (which is called 'serialization')
    # item_dict["image"] = my_item.image
    item_dict["price"] = my_item.price
    item_dict["business_id"] = my_item.business_id
    return item_dict


def buildDBItemFromJson(jsoned_item):
    ################################### MISSING: Handle images
    if ('item_name' not in jsoned_item) or ('item_desc' not in jsoned_item) or ('price' not in jsoned_item) or (
            'business_id' not in jsoned_item):
        return None
    new_item = db_item.DBItem(jsoned_item['item_name'], jsoned_item['item_desc'], None, jsoned_item['price'],
                              jsoned_item['business_id'])
    return new_item


class ItemAPI(Resource):

    def __init__(self):
        # self.reqparse = reqparse.RequestParser()
        # self.reqparse.add_argument('item_name', type = str, required = True, help = {"The requested item's name"})
        super(ItemAPI, self).__init__()

    def get(self, item_name=None):
        """Retrives the item with the provided name"""
        # item_name is a variable in the URL path (slash).
        # While request.args.get["item_name"] is the "query string" (argument) that is denoted in the URL after the question mark: http://127.0.0.1:5000/item/15/?item_name=Naseem&other_key=other_value
        try:
            if item_name is not None:
                retrieved_item = db_item.get_item(item_name)  # Firestore database

                if retrieved_item is None:
                    # Item not found in DB, or DB is down:
                    return {"error": "Item with name " + str(item_name) + " was not found!"}, 404

                item_json = retrieved_item.toJson()  # Marshmallow usage
                response = item_json, 200  # a 'request.response' type of object
                return response

        except Exception as err:
            logger.error(str(err))
            return {"error": str(err)}, 404

    def post(self):
        """Created a new item in DB"""

        # JSON data is submitted in the body of the request (in Postman: body --> raw (json))
        # request.get_json() knows how to read the json accompanied with the request.

        new_item = request.get_json()
        if new_item is None:
            logger.error("New item's json is empty")
            return {"error": "Json is empty"}, 204  # 204: No content

        """ We can read further info, for example business_id from the URL query string """
        """ request.args.get('business_id') according to how we want """

        try:
            new_item = buildDBItemFromJson(new_item)
            if new_item is None:
                return {"error": "New item's json is not valid!"}

            new_item.add_item()  # DB access
            return "Success! Item " + str(new_item.name) + " Created.", 201
        except Exception as err:
            logger.error(str(err))
            #  return {"error": str(err)}, 404
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
