"""FlaskのConfigを提供する"""
import os


class BaseConfig(object):
    # Flask
    DEBUG = False
    TESTING = False


class Development(BaseConfig):

    # Flask
    DEBUG = True
    TESTING = True

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = \
        'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8' \
        .format(**{
            'user': os.getenv('DB_USER', 'root'),
            'password': os.getenv('DB_PASSWORD', 'root'),
            'host': os.getenv('DB_HOST', 'db'),
            'database': os.getenv('DB_DATABASE', 'flask_sample'),
        })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class Testing(BaseConfig):

    # Flask
    DEBUG = True
    TESTING = True

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = \
        'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8' \
        .format(**{
            'user': os.getenv('DB_USER', 'root'),
            'password': os.getenv('DB_PASSWORD', 'root'),
            'host': os.getenv('DB_HOST', 'localhost'),
            'database': os.getenv('DB_DATABASE', 'test_flask_sample'),
        })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class Production(BaseConfig):

    # Flask
    DEBUG = True
    TESTING = True

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = \
        'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8' \
        .format(**{
            'user': os.getenv('DB_USER', 'root'),
            'password': os.getenv('DB_PASSWORD', 'root'),
            'host': os.getenv('DB_HOST', 'db'),
            'database': os.getenv('DB_DATABASE', 'production_flask_sample'),
        })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
