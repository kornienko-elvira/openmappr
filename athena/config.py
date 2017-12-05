class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'mongodb://localhost:27017/MAPPRDB'
    DATABASE = "MAPPRDB"
    BEANSTALK_HOST = "localhost"
    BEANSTALK_PORT = 11300
    BEANSTALK_PIPE = "survey_worker"

class ProductionConfig(Config):
    DATABASE_URI = 'mongodb://<HOST>:<PORT>/MAPPRDB'
    BEANSTALK_HOST = "<>"

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    DATABASE = 'MAPPR_TEST'

# create other configs here