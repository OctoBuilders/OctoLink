from flask_config import db


class User(db.Model):
    """Create user database fields

    Fields:
    id -- provides each row entry with a unique id.
    student_number -- store users 7 character student number (e.g 1342556).
    email -- store users UOB email (e.g af23467@my.bristol.ac.uk).
    faculty -- store users faculty (e.g Engineering).
    password_hash -- store sha256 hash of users password.
    """

    id = db.Column(db.Integer, primary_key=True)
    student_number = db.Column(db.String(7),  unique=True, nullable=False)
    email = db.Column(db.String(24), unique=True, nullable=False)
    faculty = db.Column(db.String(25),  nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
