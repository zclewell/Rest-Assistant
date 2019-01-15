import pychromecast
from flask import request
from flask_restful import Resource

UNKNOWN_STATE = 'UNKNOWN'
PLAYING_STATE = 'PLAYING'
PAUSED_STATE = 'PAUSED'

TOGGLE_ACTION = 'toggle'
PAUSE_ACTION = 'pause'
PLAY_ACTION = 'play'
STOP_ACTION = 'stop'

mc_dict = {}
for cc in pychromecast.get_chromecasts():
    mc_dict[cc.device.friendly_name] = cc.media_controller
print(len(mc_dict), 'Chromecasts found')

action_set = set(['play', 'pause', 'toggle', 'stop'])


class HandleChromecast(Resource):
    def get(self):
        json = {'device_ids': list(mc_dict.keys())}
        return json

    def post(self):
        good_to_run = True
        json = {'errors': []}
        device_id = request.form['device_id']
        if device_id in mc_dict:
            mc = mc_dict[device_id]
        else:
            good_to_run = False
            json['errors'].append('Device Id: ' + device_id + ' not found')
        action = request.form['action']
        if action not in action_set:
            good_to_run = False
            json['errors'].append('Action: ' + action + ' not found')
        if good_to_run:
            if action == TOGGLE_ACTION:
                toggle_mc(mc)
            elif action == PLAY_ACTION:
                play_mc(mc)
            elif action == PAUSE_ACTION:
                pause_mc(mc)
            elif action == STOP_ACTION:
                stop_mc(mc)
        else:
            return json


def wait_until_known(mc):
    while mc.status.player_state == UNKNOWN_STATE:
        continue


def toggle_mc(mc):
    wait_until_known(mc)
    if mc.status.player_state == PAUSED_STATE:
        mc.play()
    elif mc.status.player_state == PLAYING_STATE:
        mc.pause()
    return mc.status.player_state


def stop_mc(mc):
    wait_until_known(mc)
    mc.stop()


def play_mc(mc):
    wait_until_known(mc)
    mc.play()


def pause_mc(mc):
    wait_until_known(mc)
    mc.pause()
