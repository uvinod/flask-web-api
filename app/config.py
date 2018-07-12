import os

base_dir = os.path.abspath(os.path.dirname(__file__))
local_base = 'postgresql://postgres:Welcome30@localhost:5432/'
#local_base = 'mysql+pymysql://x9kd2utgayq3lg35:r2mmurz65slbsmxg@g9fej9rujq0yt0cd.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/'
database_name = 'chatbotservice'
#database_name = 'zctm7hxwfhlis4hs'


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
    