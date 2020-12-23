from __main__ import shared
import sys, os

commands = {}

def list(command):
    print(shared["content"])
commands["list"] = list

def exit(command):
    sys.exit(0)
commands["exit"] = exit

def help(command):
    print("Commands:")
    print("\tlist: list all contents")
    print("\texit: exit")
    print("\thelp: help")
commands["help"] = help

def load(command):
    file_name = command[4:].strip()
    print("Loading", file_name)
    try:
        with open(file_name, "r") as file:
            shared["content"] = file.read()
    except Exception as e:
        print("File not found:", e)
commands["load"] = load
