from flask import Flask, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://ubtwwkvidcglbysffkxi:tNzPkPdRp6PGv6HKDcHm@bqw1nnfvu8a3jff-mongodb.services.clever-cloud.com:27017/bqw1nnfvu8a3jff"
mongo = PyMongo(app)


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


if __name__ == '__main__':
    app.run()
    # app.run(debug=True)