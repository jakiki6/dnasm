import sys, os

class Logger(object):
    def __init__(self, file=sys.stdout):
        self.file = file
    def info(self, string):
        self.file.write(f"INFO: {string}\n")
    def warn(self, string):
        self.file.write(f"WARN: {string}\n")
    def debug(self, string):
        if "DEBUG" in os.environ.keys():
            self.file.write(f"DEBUG: {string}\n")
