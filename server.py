from flask import Flask
from flask_restful import Resource, Api
import pychromecast

app = Flask(__name__)
api = Api(app)

mc_dict = {}
for cc in pychromecast.get_chromecasts():
	mc_dict[cc.device.friendly_name] = cc.media_controller


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class ToggleHomeTv(Resource):
	def get(self):
		# Get the media controller from the dict
		mc = mc_dict['Home TV']

		# Can't call immediately for some reason, loop until we response
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