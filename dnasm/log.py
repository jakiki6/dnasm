import sys, os

class Logger(object):
    def __init__(self, file=sys.stderr, level=3):
        self.file = file
        self.level = level
    def debug(self, string):
        if self.level <= 0:
            self.file.write(f"DEBUG: {string}\n")
    def info(self, string):
        if self.level <= 1:
            self.file.write(f"INFO: {string}\n")
    def warn(self, string):
        if self.level <= 2:
            self.file.write(f"WARN: {string}\n")
    def fatal(self, string):
        if self.level <= 3:
            self.file.write(f"FATAL: {string}\n")
