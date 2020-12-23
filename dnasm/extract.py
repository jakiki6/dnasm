#!/bin/env python3

import argparse

from constants import *

parser = argparse.ArgumentParser(description='Extractor for ncbi.nlm.nih.gov')
parser.add_argument("--input", type=str, default="/dev/stdin")
parser.add_argument("--output", type=str, default="/dev/stdout")
parser.add_argument("--compressed", help="decompresses data from IUPAC", action="store_true")
args = parser.parse_args()

with open(args.input, "r") as file:
    raw_data = file.read()

if args.compressed:
    data = ""
    fdata = ""
    for line in raw_data.split("\n"):
        buf = ""
        for char in line:
            if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ*-":
                buf += char
        fdata += buf
    for char in fdata:
        data += IUPAC[char]
else:
    data = ""
    for line in raw_data.split("\n"):
        buf = ""
        for char in line:
            if char in "atgc":
                buf += char
        data += buf

with open(args.output, "w") as file:
    file.write(data)
