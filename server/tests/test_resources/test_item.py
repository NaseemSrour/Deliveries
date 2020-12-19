import sys 
sys.path.insert(0, '../')

from flask.testing import FlaskClient
from flask.wrappers import Response

ITEMS_URL = "/items"

def test_get_item(client: FlaskClient): 
    # get item
    response: Response = client.get(ITEMS_URL)

    # make assertions 
    assert response.status_code == 200
    
    # TODO: Obviously the following assertion should be changed once we have actual functionality here
    assert response.json == "Item Retrieved"

