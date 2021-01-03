import sys 
sys.path.insert(0, '../')
import json

from flask.testing import FlaskClient
from flask.wrappers import Response

ITEMS_URL = "/items"

def test_get_item(client: FlaskClient): 
    # get an existing item
    response: Response = client.get('/item/10')
    
    # make assertions 
    assert response.status_code == 200
    assert response.json == json.loads('''{ "item_id": 10, "item_name": "Steak 5nzer", "item_desc": "Steak 5nzer bnaqi6", "price": 33, "business_id": 1 }''')

    # Get a non-existent item
    nonExistentID = 2
    response_get_nonExist: Response = client.get('/item/' + str(nonExistentID))

    # Assertions:
    assert response_get_nonExist.status_code == 404
    assert response_get_nonExist.json == json.loads(''' {"error": "Item with ID ''' + str(nonExistentID) + ''' was not found!"} ''')
    
