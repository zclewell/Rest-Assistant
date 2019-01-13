from flask import Flask
from flask_restful import Resource, Api
from requests import put, get
import pychromecast
import time

app = Flask(__name__)
api = Api(app)
test = 'yeet'
cc_list = pychromecast.get_chromecasts()
for cc in cc_list:
	# print(test)
	if cc.device.friendly_name == 'Home TV':
		mc = cc.media_controller
		break

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class ToggleHomeTv(Resource):
	def get(self):
		# mc = self.mc
		while mc.status.player_state == 'UNKNOWN':
			continue
		if mc.status.player_state == 'PAUSED':
			mc.play()
		elif mc.status.player_state == 'PLAYING':
			mc.pause()
		return mc.status.player_state

api.add_resource(ToggleHomeTv, '/toggle')

if __name__ == '__main__':
    app.run(debug=True)
    # self.cc_list = pychromecast.get_chromecasts()
    # Refresh()