from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)

class Item(Resource):
    def get(self, name):
        return {'item': name}
    def post(self, name):
        return {'item': name}, 201
    def delete(self, name):
        return {'message': f'Item {name} deleted'}
class ItemList(Resource):
    def get(self):
        return {'items': ['Item1', 'Item2']}
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

if __name__ == '__main__':
    app.run(debug=True)
