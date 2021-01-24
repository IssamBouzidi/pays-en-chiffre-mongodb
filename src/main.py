from flask import Flask, jsonify
from flask_pymongo import PyMongo



app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://ubtwwkvidcglbysffkxi:tNzPkPdRp6PGv6HKDcHm@bqw1nnfvu8a3jff-mongodb.services.clever-cloud.com:27017/bqw1nnfvu8a3jff"
mongo = PyMongo(app)


import json
from bson import ObjectId
from bson import json_util

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

@app.route('/countries', methods=['GET'])
def get_all_countries():
    countries = mongo.db.country
    output = []
    

    for country in countries.find():
        item = {}
        item["id"] = country['_id']
        item['country'] = country['country']
        item['land_area'] = country['land_area']
        
        output.append(item)
            
    return jsonify({'result' : output})

@app.route('/countries/<country_name>', methods=['GET'])
def get_country_by_name(country_name):
    countries = mongo.db.country
    # country= countries.find_one_or_404({"country": country_name})
    country= countries.find_one({"country": country_name})
    
    # return jsonify({'result': country})
    a = parse_json(country)
    return a
    # return jsonify(country)
from bson.json_util import dumps

def parse_json(data):
    return json.loads(json_util.dumps(data))

if __name__ == '__main__':
    app.run()
    # app.run(debug=True)