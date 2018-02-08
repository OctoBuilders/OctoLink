from flask_config import db

class User(db.Model):
    id            = db.Column(db.Integer,     primary_key=True)
    username      = db.Column(db.String(7),   unique=True, nullable=False)      # eg: 'ab12345'
    email         = db.Column(db.String(21),  unique=True, nullable=False)      # eg: 'ab122345@bristol.ac.uk'
    faculty       = db.Column(db.String(25),  nullable=False)                   # eg: 'Engineering'
    password_hash = db.Column(db.String(128), nullable=False)                   #      Hash of the users password
