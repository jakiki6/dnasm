import sys
sys.path.append('../')
from constants import *
sys.path = sys.path[:-1]

def bases(line, content):
    res = line.replace("bases", "").replace(" ", "").lower()
    buf = ""
    for char in res:
        if not char in ("t", "g", "c", "a", "u"):
            raise ValueError(char + " is not a valid base!")
    return res.replace("u", "t")

def start(line, content):
    return "atg"

def end(line, content):
    return "taa" # only safe end pair because the other 2 can be interpreted as acids

def acids(line, content):
    res = [x.strip() for x in line.replace("acids", "").split(",")]
    buf = ""
    for acid in res:
        if not acid in ACIDS.keys():
            raise ValueError(char + " is not a valid amino acid!")
        buf += ACIDS[acid]  
    return buf

def tail(line, content):
    line = line.replace("tail", "")
    i = int(line)
    return "a" * i

def point(line, content):
    print(f"{line[5:]} at {len(content)}", file=sys.stderr)
    return ""

def pad(line, content):
    res = int(line[4:])
    res = res - len(content)
    if res < 0:
        print("Negative value on padding")
        res = 0
    return "a" * res
