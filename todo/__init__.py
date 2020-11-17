from flask import Flask

from .main.routes import main
from .extensions import mongo, MONGO_URI

def create_app():
    app=Flask(__name__)
    app.config['MONGO_URI']=MONGO_URI
    mongo.init_app(app)
    app.register_blueprint(main)
    return app