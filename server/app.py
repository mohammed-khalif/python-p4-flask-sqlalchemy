# app/app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///server.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False

migrate = Migrate(app, db)

db.init_app(app)

if __name__ == '__main__':
    app.run(port=5554)

