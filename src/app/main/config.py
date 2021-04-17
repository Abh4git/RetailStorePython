import os
# uncomment the line below for postgres database url from environment
# postgres_local_base = os.environ['DATABASE_URL']
basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False
class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    SQLALCHEMY_DATABASE_URI ='postgresql://localhost/retailstoredb?user=postgres&password=test' #'sqlite:///'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///'
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/retailstoredb?user=postgres&password=test'  # 'sqlite:///'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
    )

key = Config.SECRET_KEY
