import sys 
sys.path.insert(0, '../')
import json

from flask.testing import FlaskClient
from flask.wrappers import Response

ITEM_URL = "/item"

def test_get_item(client: FlaskClient): 
    # GET an existing item
    response: Response = client.get(ITEM_URL + '/' + str(10))
    
    # make assertions 
    assert response.status_code == 200
    assert response.json == json.loads('''{ "item_id": 10, "item_name": "Steak 5nzer", "item_desc": "Steak 5nzer bnaqi6", "price": 33, "business_id": 1 }''')

    # Get a non-existent item
    nonExistentID = 2
    response_get_nonExist: Response = client.get(ITEM_URL + '/' + str(nonExistentID))

    assert response_get_nonExist.status_code == 404
    assert response_get_nonExist.json == json.loads(''' {"error": "Item with ID ''' + str(nonExistentID) + ''' was not found!"} ''')

def test_post_item(client: FlaskClient):
    # POST a new item
    new_item = dict(item_name="NEW hummus", item_desc="3elbet hummus", price=15, business_id=1)
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': '*/*'
    }
    
    response: Response = client.post(ITEM_URL, data=json.dumps(new_item), headers=headers)
    
    assert response.status_code == 201
    # assert response.content_type == mimetype
    assert response.json == "Success! Item NEW hummus Created."  # Not an actual json, will switch it when we interface with the frontend later , as: {'success': 'item hummus added successfully'}
