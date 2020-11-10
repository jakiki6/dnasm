#!/bin/env python3
import sys, argparse, math

from constants import *

def strip_comments(line):
    return line.split(";")[0]
def strip_other(line):
    res = ""
    in_skip = False
    for char in line:
        if char in ("\"", "'"):
            in_skip = not in_skip
        if not in_skip and not char in ("\t", " "):
            res += char
    return res

def prepare(line):
    if line.startswith("%include"):
        path = line[9:len(line) - 2]
        with open(path, "r") as file:
            res = file.read()
        if res[len(res) - 1] != "\n":
            res += "\n"
        return res
    elif line.startswith("%protein"):
        name = line[8:]
        res = get_protein(name)
        if res[len(res) - 1] != "\n":
            res += "\n"
        return res
    else:
        return line

def parse(expression):
    if expression.startswith("times"):
        i = ""
        for char in expression[5:]:
            if not char in ("0", "1", "2" "3", "4", "5", "6", "7", "8", "9"):
                break
            i += char
        offset = 5 + len(i)
        i = int(i)
        res = ""
        for _ in range(0, i):
            res += _parse(expression[offset:])
        return res
    else:
        return _parse(expression)

def _parse(expression):
    if expression.startswith("bases"):
        res = expression[5:].replace(" ", "")
        buf = ""
        for char in res:
            if not char in ("t", "g", "c", "a"):
                raise ValueError(char + " is not a valid base!")
        return res
    elif expression.startswith("start"):
        return "atg"
    elif expression.startswith("end"):
        return "tag"
    elif expression.startswith("acids"):
        res = [x.strip() for x in expression[5:].split(",")]
        buf = ""
        for acid in res:
            if not acid in ACIDS.keys():
                raise ValueError(char + " is not a valid amino acid!")
            buf += ACIDS[acid]
        return buf
    else:
        return ""

parser = argparse.ArgumentParser(description='RNA/DNA assembler')
parser.add_argument("--input", type=str, default="/dev/stdin")
parser.add_argument("--output", type=str, default="/dev/stdout")
parser.add_argument("--manual", help="display manual", action="store_true")
parser.add_argument("--compress", help="compress genom in smaller data (4 bases per byte)", action="store_true")
args = parser.parse_args()

if args.manual:
    import os
    os.system("less manual.txt")
    exit()

result = ""

with open(args.input, "r") as file:
    content = file.read()

_content = ""

for line in content.split("\n"):
    line = strip_comments(line)
    line = strip_other(line)
    _content += prepare(line)

content = _content
result = ""

for line in content.split("\n"):
    line = strip_comments(line) 
    line = strip_other(line)   
    result += parse(line)

size = len(result)
fsize = size

while fsize > 1000:
    fsize = fsize / 100 // 1 / 10

if 0 <= size < 1000:
    fmtsize = f"{fsize} base(s)"
elif 1000 <= size <= 1000000:
    fmtsize = f"{fsize} kb"
elif 1000000 <= size <= 1000000000:
    fmtsize = f"{fsize} mb"
elif 1000000000 <= size <= 1000000000000:
    fmtsize = f"{fsize} gb"
else:
    fmtsize = f"{fsize} tb"

print(f"Output has a size of {fmtsize}.")

if args.compress:
    buf = bytearray(math.ceil(len(result) / 3))
    offset = 0
    for char in result:
        buf[offset // 8] |= MAPPING[char] << (offset % 8)
        offset += 2
    result = ""
    for char in buf:
        result += chr(char)

with open(parser.parse_args().output, "w") as file:
    file.write(result)
