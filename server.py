from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps
from scanner import Scanner

app = Flask(__name__)
api = Api(app)
scanner = Scanner()

class Scan(Resource):    
    def post(self):
        document = request.form['document']
        tokens = scanner.scan(document)
        return jsonify(tokens=[e.serialize() for e in tokens])

api.add_resource(Scan, '/scan') # Route_1

if __name__ == '__main__':
     app.run(host='0.0.0.0', port='5002')
     
