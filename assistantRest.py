from flask import request
from flask_restful import Resource
from authenticate import is_valid_key

from assistant import assistant_wrapper

assistant = assistant_wrapper.get_assistant()


class HandleQuery(Resource):
    def post(self):
        key = request.form['key']
        if not is_valid_key(key):
            return
        query = request.form['query']
        response = assistant.assist(text_query=query)[0]
        json = {'response': response}
        return json
