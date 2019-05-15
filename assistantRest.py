import json

from flask import request
from flask_restful import Resource

from assistant import assistant_wrapper
from helper import is_valid_key, get_value

assistant = assistant_wrapper.get_assistant()


class HandleQuery(Resource):
    def post(self):
        args = request.args
        body = request.form
        key = get_value(args, body, 'key')
        if not is_valid_key(key):
            return

        query = get_value(args, body, 'query')
        if query:
            response = assistant.assist(text_query=query)[0]
            json_out = {'response': response}
            return json_out
