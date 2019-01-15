key_set = set()
secret_f = open('secret')
line = secret_f.readline()
while line:
    key_set.add(line)
    line = secret_f.readline()

def is_valid_key(key):
    return key in key_set