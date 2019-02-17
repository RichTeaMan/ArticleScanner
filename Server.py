from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps
from Scanner import Scanner

app = Flask(__name__)
api = Api(app)

class Test(Resource):
    def get(self):
        return {'employees': 'test'} # Fetches first column that is Employee ID
    
    def post(self):
        json_data = request.get_json(force=True)
        doc = json_data['doc']
        scanner = Scanner()
        tokens = scanner.scan(doc)
        return jsonify(tokens=[e.serialize() for e in tokens])

api.add_resource(Test, '/test') # Route_1

if __name__ == '__main__':
     app.run(port='5002')
     
