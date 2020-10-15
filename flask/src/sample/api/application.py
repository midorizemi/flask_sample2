"""flask appの初期化を行い、flask appオブジェクトの実体を持つ"""
from flask import Flask
import os
from .functions import main
from .extensions import (db, ma, migrate)


def create_app():
    config_type = {
        "development": "api.config.Development",
        "testing": "api.config.Testing",
        "production": "api.config.Production"
    }

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(
        config_type.get(os.getenv('FLASK_ENV', 'development')))

    # app.config.from_pyfile('sensitive_data.cfg') # APIキーなど秘密情報
    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app):
    """拡張機能の初期設定する"""
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    return None


def register_blueprints(app):
    """GCP CloudFunctionのために functions/ に分けました．"""
    app.register_blueprint(main.app)


app = create_app()
