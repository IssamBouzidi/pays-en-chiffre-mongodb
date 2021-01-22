from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://ubtwwkvidcglbysffkxi:tNzPkPdRp6PGv6HKDcHm@bqw1nnfvu8a3jff-mongodb.services.clever-cloud.com:27017/bqw1nnfvu8a3jff"
mongo = PyMongo(app)