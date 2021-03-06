import sys
sys.path.append('../')
from constants import *
import utils
sys.path = sys.path[:-1]

def bases(line):
    res = "".join(line.args).lower()
    buf = ""
    for char in res:
        if not char in ("t", "g", "c", "a", "u", "Ψ"):
            raise ValueError(char + " is not a valid base!")
    return res.replace("u", "t").replace("Ψ", "t")

def start(line):
    return "atg"

def end(line):
    return "taa" # only safe end pair because the other 2 can be interpreted as acids

def acids(line):
    res = line.args
    buf = ""
    for acid in res:
        if not acid in ACIDS.keys():
            raise ValueError(char + " is not a valid amino acid!")
        buf += ACIDS[acid]  
    return buf

def tail(line):
    i = utils.req_int(line.args[0])
    return "a" * i

def pad(line):
    res = utils.req_int(line.args[0])
    if res < 0:
        print("Negative value on padding")
        res = 0
    return "a" * res

def cap(line):
    return "ga"

def linker(line):
    return "gcatatgact"

def iupac(line):
    res = ""
    for char in "".join(line.args):
        res += IUPAC[char]
    return res
