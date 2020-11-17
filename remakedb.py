from app import db, app
from models import *
with app.app_context():
    db.drop_all()
    db.create_all()