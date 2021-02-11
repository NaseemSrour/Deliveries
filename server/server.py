import logging
import logging.config
from flask import Flask
from flask_restful import Resource, Api

from resources.item_api import ItemAPI

from config.logger_config import DEFAULT_LOGGING 

logging.config.dictConfig(DEFAULT_LOGGING)
logger = logging.getLogger(__name__)
logger.debug("Logger is configured!")


def create_app() -> Flask:
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(ItemAPI, '/item', '/item/<string:item_name>', endpoint='item_api')  # endpoint shkla esm l resource (file) in lowercase
    # Maybe make the item_name parameter as a Query String (? =)
    return app 

if __name__ == '__main__':
    # The following line commented out line makes the server accessible from other PCs in the same network at port 80
    # app.run(host='0.0.0.0', port=80, debug=True)
    # Runs at localhost:5000 
    logger.info("Starting app...")
    app = create_app()

    app.run(debug=True)
