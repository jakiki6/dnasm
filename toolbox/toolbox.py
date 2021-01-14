#!/bin/env python3
import argparse, os, sys

from toolboxcmds import modes

parser = argparse.ArgumentParser(description='A toolbox for genome related stuff')
parser.add_argument("mode", type=str)
parser.add_argument("file", type=str)

args = parser.parse_args()

if not os.path.isfile(args.file):
    print(f"{args.file} is not a file", file=sys.stderr)
    exit(1)

try:
    modes[args.mode]["func"](args.file)
except KeyError:
    print("Available modes:")
    for key, val in modes.items():
        print(f"\t{key}:")
        for line in val["desc"].split("\n"):
            print(f"\t\t{line}")
