#!/bin/env python3
import os, sys, atexit

pwd = os.getcwd()
home = os.path.dirname(os.path.realpath(__file__))
libs = os.path.join(os.path.dirname(home), "lib")

sys.path.append(home)
sys.path.append(libs)

import log

if "DEBUG" in os.environ.keys():
    logger = log.Logger(level=0)
else:
    logger = log.Logger()

import dnasmcore, opcodes

try:
    import gnureadline as readline
except ImportError:
    import readline

options = list(opcodes.OPCODES.keys()) + ["times", "exit", "help"]

def complete(text, state):
    res = None
    if state == 0:
        if text:
            matches = [s for s in options if s.startswith(text)]
        else:
            matches = options[:]

    try:
        res = matches[state]
    except:
        res = None

    return res

readline.set_completer(complete)
readline.parse_and_bind("tab: complete")
readline.set_history_length(-1)
hfn = os.path.expanduser("~/.dnash_history")

if not os.path.isfile(hfn):
    os.mknod(hfn)

readline.read_history_file(hfn)

def save_history():
    readline.write_history_file(hfn)
atexit.register(save_history)

print("Try 'help' to get started")

running = True
while running:
    try:
        lines = input("> ")
    except:
        break

    code = ""
    for line in lines.split(":"):
        if line.strip() == "exit":
            running = False
            break
        elif line.strip() == "help":
            print("Use 'exit' to exit and 'help' for displaying this help\nAvailable opcodes:")
            for opcode in opcodes.OPCODES.keys():
                print(f"\t{opcode}")
            print("Lines can be comined with ':'\ne.g. 'bases gcc : align 8' -> 'gccaaaaa'", end="")
        else:
            code += line + "\n"

    try:
        print(dnasmcore.process(code))
    except SystemExit:
        pass
