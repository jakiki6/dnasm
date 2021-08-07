import utils, constants

def bases(line):
    res = "".join(line.args).lower()
    buf = ""
    for char in res:
        if not char in ("t", "g", "c", "a", "u", "ψ"):
            raise ValueError(char + " is not a valid base!")
    return res.replace("u", "t").replace("ψ", "t")

def start(line):
    return constants.ACIDS["Start"][0]

def end(line):
    return constants.ACIDS["Stop"][0]

def acids(line):
    res = line.args
    buf = ""
    for acid in res:
        if not acid in constants.ACIDS.keys():
            raise ValueError(acid + " is not a valid amino acid!")
        buf += constants.ACIDS[acid][0]  
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

def compressed(line):
    res = ""
    for char in "".join(line.args):
        res += constants.IUPAC[char][0]
    return res
