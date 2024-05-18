from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models.tables import *

from app.controllers import index
from app.controllers import brinquedos
from app.controllers import professores

#################################
# from app.controllers import admin
#################################