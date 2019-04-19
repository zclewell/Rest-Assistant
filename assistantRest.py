import json

from flask import request
from flask_restful import Resource

from assistant import assistant_wrapper
from helper import is_valid_key

assistant = assistant_wrapper.get_assistant()


class HandleQuery(Resource):
    def post(self):
        args = request.args

        key = args.get('key', False)
        if not is_valid_key(key):
            return

        query = args.get('query', False)
        if query:
            response = assistant.assist(text_query=query)[0]
            json_out = {'response': response}
            return json_out
