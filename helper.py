from logger import CustomLogger

CUSTOM_LOGGER_HEADER = 'helper'

log = CustomLogger(CUSTOM_LOGGER_HEADER).log

key_set = set()
try:
    secret_f = open('secret')
    line = secret_f.readline()
    while line:
        key_set.add(line)
        line = secret_f.readline()
except FileNotFoundError:
    log('no secret file found, all requests will be accepted')
    key_set = None


def is_valid_key(key):
    if key_set:
        return key and key in key_set
    else:
        return True


def get_value(args, body, key, useArgs=True):
    argVal = args.get(key, False)
    bodyVal = body.get(key, False)
    if argVal and bodyVal:
        if argVal == bodyVal:
            return argVal
        elif useArgs:
            return argVal
        else:
            return bodyVal
    elif argVal:
        return argVal
    elif bodyVal:
        return bodyVal
    else:
        return False
