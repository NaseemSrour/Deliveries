from flask import Flask
from flask_restful import Resource, Api

from resources.item import Item

app = Flask(__name__)
api = Api(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


api.add_resource(Item, '/items', '/items/<string:item_id>', endpoint='items')



if __name__ == '__main__':
    # The following line commented out line makes the server accessible from other PCs in the same network at port 80
    # app.run(host='0.0.0.0', port=80, debug=True)
    # Runs at localhost:5000 
    app.run(debug=True)