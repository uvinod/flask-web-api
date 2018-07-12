import os

base_dir = os.path.abspath(os.path.dirname(__file__))
local_base = 'postgresql://postgres:Welcome30@localhost:5432/'
#local_base = 'postgres://appyisypegdoef:92fca4b6df0ffe561d39164a57b90ec4a7e6267d7f066c5344242dbb2982f99d@ec2-54-227-240-7.compute-1.amazonaws.com:5432/'
database_name = 'chatbotservice'
#database_name = 'd3kcjb36e6b19a'


class BaseConfig:
    #
    #Base application configuration
    #
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    #
    #Development application configuration
    #
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', local_base + database_name)
    
class TestingConfig(BaseConfig):
    #
    #Testing application configuration
    #
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL_TEST', local_base + database_name + "_test")
    
class ProductionConfig(BaseConfig):
    #
    #Production application configuration
    #
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', local_base + database_name)
    