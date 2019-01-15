from flask import Flask
from flask_restful import Api
from assistantRest import HandleQuery
from chromeCastRest import HandleChromecast

app = Flask(__name__)
api = Api(app)

api.add_resource(HandleChromecast, '/chromecast')
api.add_resource(HandleQuery, '/assistant')

if __name__ == '__main__':
    app.run(debug=True)
