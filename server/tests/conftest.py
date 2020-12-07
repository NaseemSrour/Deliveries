import sys, os
from pathlib import Path
from typing import Generator
from testing_utils import delete_all_testbenches
parent_dir = Path((os.path.dirname(os.path.abspath(__file__)))).parent
sys.path.insert(0, str(parent_dir)) 

import pytest
from flask.testing import FlaskClient

import server   

"""
Any pytest construct defined within the conftest.py file can be accessed by all testcases within and below this directory structure. 

Fixtures are a pytest construct that can be used to encapsulate repeating functionality that can be shared across tests.

You define a fixture, that usually returns/yields some sort of an object. 
In your test function, you add an argument with the name of the fixture, then at runtime, the pytest framework injects that fixture into your test.

e.g. you can use the client from below in any test you wish, by simply supplying an arg called client to the test function:
def test_example(client):
    # here you now have access to the FlaskClient from below. You can then use it to test the backend:
    response = client.get('localhost')

    assert response.status_code == 200
    assert response.json == ...
"""

"""This fixture provides a flask test client. Currently, a new (clean) client is generated for each test function. 
This can be changed using the 'scope' keyword arg to the fixture.
"""
@pytest.fixture(scope="function")   
def client() -> Generator[FlaskClient, None, None]:
    # Test setup code be added before the yield statement and it will be executed before running the test
    server.create_app().config['TESTING'] = True
    with server.create_app().test_client() as client:
        yield client
    
    # Any code added here is "teardown" code, which will be executed, once a test finishes execution.
        
    

