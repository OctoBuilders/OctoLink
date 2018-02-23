from flask                 import Flask
from flask_sqlalchemy      import SQLAlchemy
from flask_restful         import Api
from printer_to_server_api import AddPrinter, PrintStatus

# App config
app = Flask(__name__)
app.config['SECRET_KEY']                     = 'helloworld'
app.config['SQLALCHEMY_DATABASE_URI']        = 'sqlite:///./database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database config
db = SQLAlchemy(app)

# API config
api = Api(app)
api.add_resource(AddPrinter, '/printers', endpoint='printers')
api.add_resource(PrintStatus,'/print_status', endpoint='print_status')
