import pychromecast
from flask_restful import Resource
from assistant import textinput


class HandleQuery(Resource):
    def get(self, query):
        query = query.replace('_', ' ')
        textinput.run_query(query)



