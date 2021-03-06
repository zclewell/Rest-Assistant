import json
import time

import pychromecast
from flask import request
from flask_restful import Resource

from helper import is_valid_key, get_value
from logger import CustomLogger

UNKNOWN_STATE = 'UNKNOWN'
PLAYING_STATE = 'PLAYING'
PAUSED_STATE = 'PAUSED'

TOGGLE_ACTION = 'toggle'
PAUSE_ACTION = 'pause'
PLAY_ACTION = 'play'
STOP_ACTION = 'stop'

CUSTOM_LOGGER_HEADER = 'Chromecast'

log = CustomLogger(CUSTOM_LOGGER_HEADER).log

mc_dict = {}
for cc in pychromecast.get_chromecasts():
    mc_dict[cc.device.friendly_name] = cc.media_controller

log(str.format('{0} chromecasts found', len(mc_dict)))

action_set = set(['play', 'pause', 'toggle', 'stop'])


class HandleChromecast(Resource):
    def get(self):
        args = request.args
        body = request.form
        key = get_value(args, body, 'key')
        if not is_valid_key(key):
            return
        json_out = {'device_ids': list(mc_dict.keys())}
        return json_out

    def post(self):
        args = request.args
        body = request.form
        key = get_value(args, body, 'key')
        if not is_valid_key(key):
            return

        device_id = get_value(args, body, 'device_id')
        action = get_value(args, body, 'action')
        delay = get_value(args, body, 'delay')
        if (action and
                device_id and
                action in action_set and
                device_id in mc_dict):
            if delay:
                time.sleep(int(delay))
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


def custom_logger(s):
    print(str.format('[%s]: %s', CUSTOM_LOGGER_HEADER, s))
