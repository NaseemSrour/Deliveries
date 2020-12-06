import logging
import logging.config
from flask import Flask
from flask_restful import Resource, Api

from resources.item import Item

from config.logger_config import DEFAULT_LOGGING 

logging.config.dictConfig(DEFAULT_LOGGING)
logger = logging.getLogger(__name__)
logger.debug("Logger is configured!")

app = Flask(__name__)
api = Api(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


api.add_resource(Item, '/items', '/items/<string:item_id>', endpoint='items')

logger.info("Hallo!")


if __name__ == '__main__':
    # The following line commented out line makes the server accessible from other PCs in the same network at port 80
    # app.run(host='0.0.0.0', port=80, debug=True)
    # Runs at localhost:5000 
    logger.error("Starting app")
    app.run(debug=True)