#!/bin/env python3

import sys, os, requests
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "lib"))
import utils, constants

def fetch_bin(url):
    if "DEBUG" in os.environ:
        print(f"fetch '{url}'")

    try:
        content = b""

        response = requests.get(url, stream=True)
        total_length = response.headers.get('content-length')

        if total_length is None:
            content = response.content
        else:
            dl = 0
            total_length = int(total_length)
            bar_size = os.get_terminal_size().columns - 5

            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                content += data
                done = int(bar_size * dl / total_length)
                print(f"\r[{'=' * (done - 1)}>{' ' * (bar_size - done - 1)}]  ", end="")

            print()

        return content
    except:
        print(f"Error while fetching '{url}'")
        exit(1)

def fetch(url):
    try:
        return fetch_bin(url).decode("utf-8")
    except:
        print(f"Encountered a decoding issue while fetching '{url}'")
        exit(1)

def fetch_nuccore(id):
    return fetch(f"https://www.ncbi.nlm.nih.gov/sviewer/viewer.cgi?tool=portal&save=file&db=nuccore&report=fasta&id={id}")
        

modes = {}

def human_genome():
    import gzip
    base = "http://hgdownload.cse.ucsc.edu/goldenpath/hg19/chromosomes/chr{}.fa.gz"

    links = {}
    for i in range(1, 23):
        links[f"chr{i}.dna"] = base.format(i)
    links["chrX.dna"] = base.format("X")
    links["chrY.dna"] = base.format("Y")

    if not os.path.isdir("human"):
        os.mkdir("human")

    for fn, link in links.items():
        print(f"Downloading {fn}...")
        data = fetch_bin(link)

        print(f"Decompressing {fn}...")
        data = gzip.decompress(data)

        print(f"Stripping {fn}...")
        data = utils.strip_fasta(data.decode())

        with open(os.path.join("human", fn), "w") as file:
            file.write(data)
modes["human-genome"] = {"func": human_genome, "desc": "Downloads all human chromosomes"}

def cat_genome():
    links = {"a1": "CM001378.3", "a2": "CM001379.3", "a3": "CM001380.3", "b1": "CM001381.3", "b2": "CM001382.3", "b3": "CM001383.3",  "b4": "CM001384.3", "c1": "CM001385.3",  "c2": "CM001386.3", "d1": "CM001387.3",  "d2": "CM001388.3",  "d3": "CM001389.3",  "d4": "CM001390.3", "e1": "CM001391.3", "e2": "CM001392.3", "e3": "CM001393.3", "f1": "CM001394.3",  "f2": "CM001395.3", "x": "CM001396.3"}

    if not os.path.isdir("cat"):
        os.mkdir("cat")

    for fn, link in links.items():
        print(f"Downloading {fn}...")
        data = fetch_nuccore(link)

        print(f"Stripping {fn}...")
        data = utils.strip_fasta(data)

        with open(f"cat/chr{fn.upper()}.dna", "w") as file:
            file.write(data)
modes["cat-genome"] = {"func": cat_genome, "desc": "Downloads all chromosomes of a cat (felis catus to be precise)"}

def dog_genome():
    links = {}
    ptr = 100
    format = "CM025{}.1"

    for i in (list(range(1, 39)) + ["X", "Y", "MT"]):
        links[str(i)] = format.format(str(ptr).zfill(3))
        ptr += 1

    if not os.path.isdir("dog"):
        os.mkdir("dog")

    for fn, link in links.items():
        print(f"Downloading {fn}...")
        data = fetch_nuccore(link)

        print(f"Stripping {fn}...")
        data = utils.strip_fasta(data)

        with open(f"dog/chr{fn.upper()}.dna", "w") as file:
            file.write(data)
modes["dog-genome"] = {"func": dog_genome, "desc": "Downloads all chromosomes of a dog (canis familiaris to be precise)"}

def usage():
    print(sys.argv[0], "<mode>")

    print("Available modes:")
    for key, val in modes.items():
        print(f"\t{key}")
        for line in val["desc"].split("\n"):
            print(f"\t\t{line}")

    exit(1)

if len(sys.argv) < 2:
    usage()

if sys.argv[1] in modes.keys():
    modes[sys.argv[1]]["func"]()
else:
    usage()
