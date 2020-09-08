import os

basedir = os.path.abspath(os.path.dirname(__file__))
db_host = os.environ.get('DATABASE_HOST')
db_port = os.environ.get('DATABASE_PORT')
db_name = os.environ.get('DATABASE_NAME')
db_pass = os.environ.get('DATABASE_PASSWORD')
db_user = os.environ.get('DATABASE_USER')


class Config:

    SQLALCHEMY_DATABASE_URI = 'postgresql://' + db_user + ':' + \
                                                db_pass + '@' + \
                                                db_host + ':' + \
                                                db_port + '/' + \
                                                db_name
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = False
    TESTING = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'test.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestConfig,
    'default': DevelopmentConfig
}
