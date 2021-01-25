from flask import Flask, jsonify
from flask_pymongo import PyMongo
import random
import datetime
import json
import simplejson as json
from bson import json_util
from bson.json_util import dumps
from bson import ObjectId
from utils import Utils
from database import Database


app = Flask(__name__) 

@app.route('/countries/all', methods=['GET'])
def get_all_countries():
    """
    get all countries
    Returns:
        json object: list of all countries
    """
    # get database instance
    db = Database.get_db(app)

    # get country collection
    countries = db.country

    # get all countries
    results = countries.find({}, {"_id": 0})
    json_results = []

    # add countries to an array
    for result in results:
        json_results.append(result)
    
    return Utils.parse_json(Utils.toJson(json_results)) #Utils.toJson(json_results)
    # return json.dumps({'x': decimal.Decimal('5.5')}, cls=DecimalEncoder)



@app.route('/countries/one/<country_name>', methods=['GET'])
def get_country_by_name(country_name):
    """
    search a country by name for:
    créer une fonction qui retourne le pays qui correspond au critère passé en paramètre. Ce paramètre est le nom du pays
    Args:
        country_name (string): name of country
    Returns:
        Json object: informations about a country
    """
    # get database instance
    db = Database.get_db(app)

    # get country collection
    countries = db.country

    # get country by name
    country= countries.find_one({"country": country_name})

    return Utils.parse_json(country)
        


@app.route('/countries/new/<country_name>', methods=['POST'])
def add_new_country(country_name):
    """
    add a new country for:
    créer une fonction qui insert un nouveau pays avec des données random (on précise uniquement le pays)
    and
    mettre la date de l'insertion lors d'une création
    Args:
        country_name (string): name of the new country to add
    Returns:
        json object: informations about new added country
    """
    # get database instance
    db = Database.get_db(app)

    # get country collection
    countries = db.country

    # create a new country with random values
    country = { 
        "country" : country_name, 
        "population" : random.randint(800, 1438207241), 
        "yearly_change" : round(random.uniform(-2.47, 3.84),2), 
        "net_change" : random.randint(0, 26337), 
        "density" : random.randint(0 , 26337), 
        "land_area" : random.randint(0 , 16376870), 
        "migrants" : random.randint(-653249 , 954806), 
        "fert_rate" : round(random.uniform(1.10 , 7),2), 
        "med_age" : random.randint(15 , 48), 
        "urban_pop" : random.randint(0 , 100), 
        "world_share" : round(random.uniform(0 , 18.47),2), 
        "date_insertion" : datetime.datetime.utcnow()
    }
    # insert the new country and get inserted id
    country_id = countries.insert_one(country).inserted_id

    # get and return the added country
    added_country = countries.find_one({"_id":ObjectId(country_id)}, {"_id": 0})
    return added_country


@app.route('/countries/by_tranche', methods=['GET'])
def get_countries_by_tranche():
    """
    get all countries grouped by tranche of density for:
    réaliser une fonction pour retourner les pays qui sont regroupés par 4 tranches (à definir) de densité de population
    Returns:
        json object: list of all countries grouped by tranche of density
    """
    # get database instance
    db = Database.get_db(app)

    # get country collection
    countries_db = db.country

    # get all countries with only name and density
    countries = countries_db.find({}, {"_id": 0, "country": 1, "density": 1 })
    output = []
    
    # fill an array with objects with only name and density tranche
    for country in countries:
        item = {}
        item['country'] = country['country']
        item['tranche'] = Utils.get_tranche(country['density'])
        
        output.append(item)
    
    # return the list of countries with tranche of density
    return jsonify({'result' : output})



if __name__ == '__main__':
    app.run(debug=True)