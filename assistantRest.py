import json

from flask import request
from flask_restful import Resource

from assistant import assistant_wrapper
from helper import is_valid_key

assistant = assistant_wrapper.get_assistant()


class HandleQuery(Resource):
    def post(self):
        json_in = json.loads(request.form['data'])

        if not is_valid_key(json_in.get('key', False)):
            return

        query = json_in.get('query', False)
        if query:
            response = assistant.assist(text_query=query)[0]
            json_out = {'response': response}
            return json_out
