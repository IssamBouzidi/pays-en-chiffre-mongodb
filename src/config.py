import os
class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
class ProductionConfig(Config):
    DEBUG = False
class DevelopmentConfig(Config):
    ENV = "development"
    DEVELOPMENT = True
    SECRET_KEY = "secret_for_test_environment"
    OAUTHLIB_INSECURE_TRANSPORT = True
class Database(Config):
    MONGODB_ADDON_URI= os.environ.get("MONGODB_ADDON_URI")