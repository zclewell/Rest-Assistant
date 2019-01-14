from flask_restful import Resource
from assistant import assistant_wrapper

assistant = assistant_wrapper.get_assistant()


class HandleQuery(Resource):
    def get(self, query):
        query = query.replace('_', ' ')
        return assistant.assist(text_query=query)
