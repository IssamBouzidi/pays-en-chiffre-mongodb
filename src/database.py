from flask_pymongo import PyMongo
from flask import Flask
import os
from config import Database as db_config


class Database:
    __instance = None
    @staticmethod 
    def getInstance():
        """ Static access method. """
        if Database.__instance == None:
            Database()
        return Database.__instance
    @staticmethod 
    def get_db(app):
        app.config["MONGO_URI"] = Database.getInstance()
        mongo = PyMongo(app)
        return mongo.db
    def __init__(self):
        """ Virtually private constructor. """
        if Database.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Database.__instance = db_config.MONGODB_ADDON_URI