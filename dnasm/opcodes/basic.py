import utils, constants

def bases(line, rna):
    res = "".join(line.args).lower()
    buf = ""
    for char in res:
        if not char in ("t", "g", "c", "a", "u", "ψ"):
            raise ValueError(char + " is not a valid base!")
    return res.replace("u", "t").replace("ψ", "t")

def start(line, rna):
    return constants.ACIDS["Start"][0]

def end(line, rna):
    return constants.ACIDS["Stop"][0]

def acids(line, rna):
    res = line.args
    buf = ""
    for acid in res:
        if not acid in constants.ACIDS.keys():
            raise ValueError(acid + " is not a valid amino acid!")
        buf += constants.ACIDS[acid][0]  
    return buf

def pad(line, rna):
    if len(line.args) < 1:
        raise ValueError("Missing value")

    res = utils.req_int(line.args[0])
    if res < 0:
        print("Negative value on padding")
        res = 0
    return "a" * res

tail = pad

def cap(line, rna):
    return "ga"

def linker(line, rna):
    return "gcatatgact"

def compressed(line, rna):
    res = ""
    for char in "".join(line.args):
        res += constants.IUPAC[char][0]
    return res

def align(line, rna):
    if len(line.args) < 1:
        raise ValueError("Missing value")

    i = utils.req_int(line.args[0]) - len(rna)
    if i < 0:
        raise ValueError(f"value {i} is smaller than 0")
    return "a" * i

def sig(line, rna):
    i = int.from_bytes(line.args[0].encode(), "little")
    res = ""

    for _ in range(0, len(line.args[0]) * 4):
        res += constants.RMAPPING[i & 0b11]
        i >>= 2

    return res
