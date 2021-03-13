from __main__ import shared
import sys, os, hashlib, json

shared["analysed"] = None

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

def loadfile(command):
    file_name = command[4:].strip()
    print("Loading", file_name)
    try:
        with open(file_name, "r") as file:
            shared["content"] = file.read()
        shared["analysed"] = None
    except FileNotFoundException as e:
        print("File not found:", e)
commands["file"] = loadfile

def analyse(command):
    shared["analysed"] = {}
    tmp = {}
    state = 1
    lindex = 0
    cstring = ""
    index = 0
    while index < len(shared["content"]):
        base = shared["content"][index:index+2]
        if base == "atg" and state == 1:
            state = 3
            cstring = ""
            lindex = index
        elif base in ("tag", "tga", "taa") and state == 3:
            state = 1
            cstring += base
            tmp[f"t_{len(tmp.keys())}"] = {"string": cstring, "index": lindex}
            index += state
            continue

        index += state

        cstring += base

    shared["analysed"]["strings"] = tmp

    shared["analysed"]["stats"] = {}
    shared["analysed"]["stats"]["strings_found"] = len(shared["analysed"]["strings"])
commands["analyse"] = analyse

def stats(command):
    if shared["analysed"] == None:
        print("Run analyse first")
        return

    print("Strings:", shared["analysed"]["stats"]["strings_found"])
    for key, val in shared["analysed"]["strings"].items():
        print(f"\t{key}: {len(val['string'])} from {val['index']} to {len(val['string']) + val['index']}")
commands["stats"] = stats

def peek(command):
    name = command[4:].strip()
    if shared["analysed"] == None:
        print("Run analyse first")
        return

    if not name in shared["analysed"]["strings"].keys():
        print(name, "not found")
    else:
        print(shared["analysed"]["strings"][name]["string"][:30] + "...")
commands["peek"] = peek

def rename(command):
    src, dest = command[6:].strip().split(" ")
    if not src in shared["analysed"]["strings"].keys():
        print(src, "does not exist")
    elif dest in shared["analysed"]["strings"].keys():
        print(dest, "exists")
    else:
        shared["analysed"]["strings"][dest] = shared["analysed"]["strings"][src]
        del shared["analysed"]["strings"][src]
commands["rename"] = rename

def save(command):
    file_name = command[4:].strip()
    with open(file_name, "w") as file:
        file.write(json.dumps(shared))
commands["save"] = save

def load(command):
    file_name = command[4:].strip()
    try:
        with open(file_name, "r") as file:
            shared.clear()
            tmp = json.load(file)
            for key, val in tmp.items():
                shared[key] = val
    except:
        print("File not found")
commands["load"] = load

def visualise(command):
    width, _ = os.get_terminal_size(0)
    bar = ["#" for _ in range(0, width)]

    for _, val in shared["analysed"]["strings"].items():
        for i in range(round(val["index"] / len(shared["content"]) * width), round((val["index"] + len(val["string"])) / len(shared["content"]) * width)):
            bar[i] = "@"

    print("".join(bar))
commands["visualise"] = visualise

def delete(command):
    name = command[4:].strip()
    if shared["analysed"] == None:
        print("Run analyse first")
        return

    if not name in shared["analysed"]["strings"].keys():
        print(name, "not found")
    else:
        del shared["analysed"]["strings"][name]
commands["del"] = delete
