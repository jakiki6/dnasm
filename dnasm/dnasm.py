#!/bin/env python3
import sys, argparse, math, os
import log

if "DEBUG" in os.environ.keys():
    logger = log.Logger(level=0)
else:
    logger = log.Logger()

pwd = os.getcwd()
home = os.path.dirname(os.path.realpath(__file__))

os.chdir(home)

from constants import *
from opcodes import OPCODES

os.chdir(pwd)

def strip_comments(line):
    return line.split(";")[0].split("#")[0]
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
        path = line[8:]
        with open(path, "r") as file:
            res = file.read()
        if res[len(res) - 1] != "\n":
            res += "\n"
        return res
    else:
        return line

def parse(expression):
    logger.debug(f"Parsing expression: {expression}")
    if expression.startswith("times"):
        i = ""
        logger.debug(f"Extracting number from {expression.replace('times', '').replace(' ', '').replace('    ', '')}")
        for char in expression.replace("times", "").replace(" ", "").replace("\t", ""):
            try:
                int(char)
            except:
                break
            i += char
        logger.debug(f"Got {i}")
        offset = 5 + len(i)
        i = int(i)
        res = ""
        for _ in range(0, i):
            res += _parse(expression[offset:])
        return res
    else:
        return _parse(expression)

def _parse(expression):
    for key, val in OPCODES.items():
        if expression.startswith(key):
            return val(expression)
    if expression == "":
        return ""
    logger.warn(f"Unknown expression: {expression}")
    return ""

parser = argparse.ArgumentParser(description='RNA/DNA assembler')
parser.add_argument("--input", "-i", type=str, default="/dev/stdin")
parser.add_argument("--output", "-o", type=str, default="/dev/stdout")
parser.add_argument("--manual", "-m", help="display manual", action="store_true")
parser.add_argument("--compress", "-c", help="compress genom in smaller data (4 bases per byte)", action="store_true")
parser.add_argument("--rna", "-r", help="convert it to rna (replaces t with u)", action="store_true")
args = parser.parse_args()

if args.manual:
    os.chdir(home)
    os.system("less manual.txt")
    exit()

result = ""

with open(args.input, "r") as file:
    content = file.read()

_content = ""

for line in content.split("\n"):
    line = strip_comments(line)
    line = strip_other(line)
    if line.strip() == "":
        continue
    _content += prepare(line) + "\n"

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

logger.info(f"Output has a size of {fmtsize}.")

if args.rna:
    result = result.replace("t", "u")

if args.compress:
    buf = bytearray(math.ceil(len(result) / 4))
    offset = 0
    for char in result:
        buf[offset // 8] |= MAPPING[char] << (offset % 8)
        offset += 2
    result = ""
    for char in buf:
        result += chr(char)

with open(parser.parse_args().output, "w") as file:
    file.write(result)
