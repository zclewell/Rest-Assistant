import pychromecast
from authenticate import is_valid_key
from flask import request
from flask_restful import Resource
import json
import os
import time

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
        key = request.form['key']
        if not is_valid_key(key):
            return
        json_out = {'device_ids': list(mc_dict.keys())}
        return json_out

    def post(self):
        json_in = json.loads(request.form['data'])

        if not is_valid_key(json_in.get('key', False)):
            return

        device_id = json_in.get('device_id', False)
        action = json_in.get('action', False)
        if (action and
            device_id and
            action in action_set and
            device_id in mc_dict):
            mc = mc_dict[device_id]
            if action == TOGGLE_ACTION:
                toggle_mc(mc)
            elif action == PLAY_ACTION:
                play_mc(mc)
            elif action == PAUSE_ACTION:
                pause_mc(mc)
            elif action == STOP_ACTION:
                stop_mc(mc)


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
