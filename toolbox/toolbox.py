#!/bin/env python3
import argparse, os, sys

from toolboxcmds import modes

def usage():
    print("Please specify a mode!")
    print("Available modes:")
    for key, val in modes.items():
        print(f"\t{key}:")
        for line in val["desc"].split("\n"):
            print(f"\t\t{line}")

try:
    modes[sys.argv[1]]["func"]()
except KeyError:
    usage()
except IndexError:
    usage()
