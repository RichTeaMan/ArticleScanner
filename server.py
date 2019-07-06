from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps
from scanner import Scanner

app = Flask(__name__)
api = Api(app)
scanner = Scanner()

class Info(Resource):
    def get(self):
        return 'Document scanner. Refer to https://github.com/RichTeaMan/DocumentScanner for usage information.'

class Scan(Resource):    
    def post(self):
        document = request.form['document']
        tokens = scanner.scan(document)
        return jsonify(tokens=[e.serialize() for e in tokens])

class ScanUpload(Resource):
    def post(self):
        documentFile = request.files['document']
        document = documentFile.read().decode("utf-8")
        tokens = scanner.scan(document)
        return jsonify(tokens=[e.serialize() for e in tokens])

api.add_resource(Info, '/')
api.add_resource(Scan, '/scan')
api.add_resource(ScanUpload, '/scanUpload')

if __name__ == '__main__':
     app.run(host='0.0.0.0', port='5002')
     
