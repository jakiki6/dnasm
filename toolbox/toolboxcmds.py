import sys, os, requests, random
cwd = os.getcwd()
os.chdir(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(os.path.join(os.getcwd(), "..", "lib"))
import database, utils
sys.path = sys.path[:-1]
sys.path.append(os.path.join(os.getcwd(), "..", "dnasm"))
from constants import ACIDS
sys.path = sys.path[:-1]
os.chdir(cwd)

def require(num, usage):
    if len(sys.argv) - 2 != num:
        print(sys.argv[0], "<mode>", usage)
        exit(1)
    return sys.argv[2:]

def get_file_content(file, mode="r"):
    try:
        with open(file, mode) as f:
            return f.read()
    except:
        print(file, "not found")
        exit(1)

import hashlib

modes = {}

def nop():
    require(0, "")
    pass
modes["nop"] = {"func": nop, "desc": "No operation\nJust for testing"}

def build_snippet():
    file = require(1, "<file>")[0]
    data = get_file_content(file, "rb")
    print(f"Building snippet object {database.save_raw_object(database.build_data_object(data))}")
modes["build_snippet"] = {"func": build_snippet, "desc": "Builds rna into the snippet format"}

def partition_genome():
    infile, outfile = require(2, "<input file> <output file>")
    data = get_file_content(infile)

    asm = ""

    while True:
        try:
            area = input("Area in genome (e.g. 1..10): ").split("..")
            start = int(area[0]) - 1
            end = int(area[1]) - 1

            name = input("Name of protein: ")
            comments = ""
            while True:
                a = input("Comment: ")
                if a != "":
                    comments += "; " + a + "\n"
                else:
                    break

            asm += f"; name: {name}\n; from {start} to {end}\n{comments}bases {data[start:end]}\n"
            
        except KeyboardInterrupt:
            break
        except:
            pass
    with open(outfile, "w") as file:
        file.write(asm)
modes["partition_genome"] = {"func": partition_genome, "desc": "Tool to split huge genome into sections and label them"}

def build_assembly_from_nih():
    name, outfile = require(2, "<id> <output file>")

    buf = requests.get(f"https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id={name}").content.decode()

    if buf.startswith("Failed"):
        print(f"{name} not found in database")
        exit(2)

    data = utils.tabs2dict(buf)

def mutate_genome():
    filename, mode, ratio = require(3, "<file name> <mode> <ratio>")

    try:
        ratio = float(ratio)
        assert 0 <= ratio <= 100
    except:
        print(f"Invalid ratio")

    data = get_file_content(filename)
    mdata = ""

    if mode == "randomly":
        for char in data:
            if random.randint(0, 99) < ratio:
                char = random.choice("tcag")
            mdata += char
    elif mode == "safe":
        for i in range(0, len(data), 3):
            trip = data[i:i+2]
            if random.randint(0, 99) < ratio:
                for key, val in ACIDS.items():
                    if trip in val:
                        trip = random.choice(val)
            mdata += trip
    else:
        print("Invalid mode!")
        return

    with open(filename, "w") as file:
        file.write(mdata)

modes["mutate_genome"] = {"func": mutate_genome, "desc": "Randomly mutate genome by given ratio (e.g 2.0 for 2%)\nModes:\n\tnatural: randomly mutates\n\tsafe: the built protein stays the same"}
