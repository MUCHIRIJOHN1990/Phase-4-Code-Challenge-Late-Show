from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from models import db
from routes import api_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(api_bp, url_prefix='/')

db.init_app(app)
migrate = Migrate(app, db)
