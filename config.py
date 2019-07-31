import os
from neomodel import config as neoconfig 

basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_strong_key')
    FILE_UPLOAD_PATH = os.getenv('FILE_UPLOAD_PATH', '/data')
    neoconfig.DATABASE_URL = os.environ["NEO4J_BOLT_URL"]

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    

class TestingConfig(BaseConfig):
    TESTING = True
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False

config = {
'development': DevelopmentConfig,
'testing': TestingConfig,
'production': ProductionConfig,
'default': DevelopmentConfig
}