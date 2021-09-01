#!/usr/bin/env python3
import sys, argparse, math, os
import log

if "DEBUG" in os.environ.keys():
    logger = log.Logger(level=0)
else:
    logger = log.Logger()

pwd = os.getcwd()
home = os.path.dirname(os.path.realpath(__file__))
libs = os.path.join(os.path.dirname(home), "lib")

sys.path.append(home)
sys.path.append(libs)

import dnasmcore
import constants

parser = argparse.ArgumentParser(description='RNA/DNA assembler')
parser.add_argument("input", nargs="?", type=str)
parser.add_argument("--output", "-o", type=str, default="/dev/stdout")
parser.add_argument("--compress", "-c", help="compress genom in smaller data (4 bases per byte)", action="store_true")
parser.add_argument("--rna", "-r", help="convert it to rna (replaces t with u)", action="store_true")
parser.add_argument("--version", "-v", help="print version", action="store_true")
args = parser.parse_args()

if args.version:
    print("dnasm from the dnasm project v1.0\nCopyright (C) 2021 Jakob Kirsch\nThis is free software; see the source for license conditions.")
    exit()

if not args.input:
    parser.print_help()
    exit()

with open(args.input, "r") as file:
    content = file.read()

result = dnasmcore.process(content)

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
result = result.replace("n", "a")

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
