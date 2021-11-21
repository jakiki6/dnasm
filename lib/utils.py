import math, subprocess, os
import constants

debug = "DEBUG" in os.environ

def tabs2dict(buf):
    _buf = buf.split("\n")
    buf = []
    for line in buf:
        if line.strip() != "":
            buf.append(line)
    del _buf
    level = 0
    data_stack = []
    name_stack = []
    data = {}

    for line in buf:
        clevel = get_level(line)
        # todo

def get_level(line):
    level = 0
    for char in line:
        if char == " ":
            level += 1
        else:
            break
    return level

def get_entropy(data):
    entropy = 0

    if data:
        length = len(data)

        seen = {"a": 0, "t": 0, "c": 0, "g": 0}
        for base in data:
            seen[base] += 1

        for x in "atcg":
            p_x = float(seen[x]) / length
            if p_x > 0:
                entropy -= p_x * math.log(p_x, 2)

    return (entropy / 2)

def resize(ilist, tsize):
    if len(ilist) == tsize:
        return ilist

    if len(ilist) < tsize:
        rlist = []

        for i in range(0, tsize):
            rlist.append(ilist[round(i / tsize * (len(ilist) - 1))])

        return rlist
    else:
        vals = []
        for i in range(0, tsize):
            vals.append([])

        for i in range(0, len(ilist)):
            vals[round(i / len(ilist) * (tsize - 1))].append(ilist[i])

        rlist = []
        for val in vals:
            rlist.append(sum(val) / len(val))

        return rlist

def strip_fasta(data):
    cdata = ""

    for line in data.split("\n"):
        if line.startswith(";") or line.startswith(">"):
            continue

        for char in line.lower():
            if char == "n":
                char = "a"

            if char in "atcg":
                cdata += char

    return cdata

def get_native_dir():
    return os.path.join(os.path.dirname(__file__), "..", "native")

def get_native_binary(name):
    return os.path.join(get_native_dir(), name)

def has_native(name):
    if "NONATIVE" in os.environ:
        return False

    binary = get_native_binary(name)
    return os.path.isfile(binary) or os.path.islink(binary)

def call_native(name, args):
    binary = get_native_binary(name)

    if debug:
        print(" ".join([binary, *args]))

    if not has_native(name):
        return b"", False

    proc = subprocess.run([binary, *args], stdout=subprocess.PIPE)
    if proc.returncode != 0:
        return b"", False

    return proc.stdout.decode(), True

def groups(string, size=3):
    res = []

    for i in range(0, len(string), size):
        res.append(string[i:i+size])

    return res

def find_orfs(string):
    content = "nnn" + string

    orfs = []

    for i in range(0, 3):
        pairs = groups(content[i:])

        has_start = False
        is_open = True
        for pair in pairs:
            has_start |= (pair in constants.ACIDS["Start"])

            if pair in constants.ACIDS["Stop"]:
                if not has_start:
                    is_open = False
                break

        if is_open:
            orfs.append(i)

    return orfs
