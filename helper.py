key_set = set()
secret_f = open('secret')
line = secret_f.readline()
while line:
    key_set.add(line)
    line = secret_f.readline()

def is_valid_key(key):
    return (len(key) == 0) or (key and key in key_set)

class CustomLogger:
    def __init__(self, s):
        self.s = s

    def log(self, s):
        print(str.format('[{0}]: {1}', self.s, s))