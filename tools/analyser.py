#!/bin/env python3
import sys

shared = {}

try:
    with open(sys.argv[1], "r") as file:
        shared["content"] = file.read()
except:
    pass

commands = {}
import analysercmds
commands |= analysercmds.commands

while True:
    try:
        command = input("cmd> ")
    except:
        break

    found = False
    for item, val in commands.items():
        if command.startswith(item):
            found = True
            val(command)
            break
    if not found:
        print("Not found:", command)
