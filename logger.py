class CustomLogger:
    def __init__(self, s):
        self.s = s

    def log(self, s):
        print(str.format('[{0}]: {1}', self.s, s))
