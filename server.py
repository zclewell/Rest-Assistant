from flask import Flask, request
from flask_restful import Api
from chromeCastRest import HandleChromecast

app = Flask(__name__)
api = Api(app)

api.add_resource(HandleChromecast, '/chromecast/<string:name>/<string:action>')


if __name__ == '__main__':
    app.run(debug=True)
