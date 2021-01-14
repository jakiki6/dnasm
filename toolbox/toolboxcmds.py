import sys, os
cwd = os.getcwd()
os.chdir(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(os.path.join(os.getcwd(), "..", "lib"))
import database
sys.path = sys.path[:-1]
os.chdir(cwd)

import hashlib

modes = {}

def nop(file):
    pass
modes["nop"] = {"func": nop, "desc": "No operation\nJust for testing"}

def build_snippet(file):
    with open(file, "rb") as f:
        data = f.read()
    print(f"Building snippet object {database.save_raw_object(database.build_data_object(data))}")
modes["build_snippet"] = {"func": build_snippet, "desc": "Builds rna into the snippet format"}
