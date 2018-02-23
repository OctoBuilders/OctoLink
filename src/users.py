from flask_config import db

class User(db.Model):
    """Create user database fields

    Fields:
    id -- provides each row entry with a unique id.
    student_number -- store users 7 character student number (e.g 1342556).
    email -- store users UOB email (e.g af23467@bristol.ac.uk).
    faculty -- store users faculty (e.g Engineering).
    password_hash -- store sha256 hash of users password.
    """
    id            = db.Column(db.Integer,     primary_key=True)
    username      = db.Column(db.String(7),   unique=True, nullable=False)      # eg: 'ab12345'
    email         = db.Column(db.String(21),  unique=True, nullable=False)      # eg: 'ab122345@bristol.ac.uk'
    faculty       = db.Column(db.String(25),  nullable=False)                   # eg: 'Engineering'
    password_hash = db.Column(db.String(128), nullable=False)                   #      Hash of the users password
