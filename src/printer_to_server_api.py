from flask         import request
from flask_restful import Resource, reqparse

class AddPrinter(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('key', type=str, required=True, location='json')

    def post(self):
        """
        Gets hit by a printer that has just come online
        and is sending its address and API key.
        """

        payload = self.reqparse.parse_args()
        key     = payload['key']
        ip      = request.remote_addr

        if key != 'none':
            print("New Printer at", ip, " with key: ", key)
        return 200

class PrintStatus(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('status',  type=str, required=True, location='json')
        self.reqparse.add_argument('message', type=str, required=True, location='json')

    def post(self):
        """
        Used to to infom OctoLink wheter a print has finished or failed
        """
        payload = self.reqparse.parse_args()
        status  = payload['status']
        message = payload['message']

        print(status)

        return 200
