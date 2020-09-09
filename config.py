import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = False
    TESTING = False
    MAIL_SUBJECT_PREFIX = 'Test task'
    MAIL_SENDER = 'lavrusenko oleksandr'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_PORT = 465
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SSL_DISABLE = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True or os.getenv('DEBUG')


class ProdConfig(Config):
    DEVELOPMENT = False
    DEBUG = False

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'test.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestConfig,
    'default': DevelopmentConfig,
    'prod': ProdConfig
}
