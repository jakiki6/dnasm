import sys
sys.path.append('../')
from constants import *
sys.path = sys.path[:-1]

def bases(line):
    res = line.replace("bases", "").replace(" ", "").lower()
    buf = ""
    for char in res:
        if not char in ("t", "g", "c", "a", "u"):
            raise ValueError(char + " is not a valid base!")
    return res.replace("u", "t")

def start(line):
    return "atg"

def end(line):
    return "taa" # only safe end pair because the other 2 can be interpreted as acids

def acids(line):
    res = [x.strip() for x in line.replace("acids", "").split(",")]
    buf = ""
    for acid in res:
        if not acid in ACIDS.keys():
            raise ValueError(char + " is not a valid amino acid!")
        buf += ACIDS[acid]  
    return buf

def tail(line):
    line = line.replace("tail", "")
    i = int(line)
    return "a" * i
