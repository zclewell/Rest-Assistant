key_set = set()
secret_f = open('secret')
line = secret_f.readline()
while line:
    key_set.add(line)
    line = secret_f.readline()

def is_valid_key(key):
    return key and key in key_set

class CustomLogger:
    def __init__(self, s):
        self.s = s

    def log(self, s):
        print(str.format('[{0}]: {1}', self.s, s))

def get_value(args, body, key, useArgs=True):
    argVal  = args.get(key, False)
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