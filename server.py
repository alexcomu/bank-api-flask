from flask import redirect, Flask, jsonify, abort, request, make_response, url_for
from pymongo import MongoClient
from flask_restful import Api, Resource

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client.bank

class Bank(Resource):
    def get(self):
        data = db.bank.find({},{"_id": 0})
        banks = [b for b in data]
        return jsonify( { 'data': banks } )

class Data(Resource):
    def get(self, bank_id=None):
        bank = db.bank.find_one({"BANK_ID": bank_id}, {"_id": 0})
        if not bank:
            return redirect(url_for("bank"))
        data = db.data.find({"BANK": bank['BANK']},{"_id": 0})
        response = [d for d in data]
        return jsonify( { 'data': response, 'bank': bank } )

class Index(Resource):
    def get(self):
        return redirect(url_for("bank"))

api = Api(app)
api.add_resource(Index, "/", endpoint="index")
api.add_resource(Bank, "/banks")
api.add_resource(Data, "/data/<int:bank_id>")

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=5000)

