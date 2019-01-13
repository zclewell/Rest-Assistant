import pychromecast
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
    def get(self, name, action):
        name = name.replace('_', ' ')
        if name in mc_dict:
            mc = mc_dict[name]
        else:
            return 'Name: ' + name + ' not found'

        low_action = action.lower()
        if low_action in action_set:
            if low_action == TOGGLE_ACTION:
                toggleMc(mc)
            elif low_action == PAUSE_ACTION:
                pauseMc(mc)
            elif low_action == PLAY_ACTION:
                playMc(mc)
            elif low_action == STOP_ACTION:
                stopMc(mc)
            return 'Ran ' + action + ' on ' + name
        else:
            return 'Action: ' + action + ' not found'


def waitUntilKnown(mc):
    while mc.status.player_state == UNKNOWN_STATE:
        continue


def toggleMc(mc):
    waitUntilKnown(mc)
    if mc.status.player_state == PAUSED_STATE:
        mc.play()
    elif mc.status.player_state == PLAYING_STATE:
        mc.pause()
    return mc.status.player_state


def stopMc(mc):
    waitUntilKnown(mc)
    mc.stop()


def playMc(mc):
    waitUntilKnown(mc)
    mc.play()


def pauseMc(mc):
    waitUntilKnown(mc)
    mc.pause()
