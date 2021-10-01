#!/bin/env python3

import sys, os, requests
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "lib"))
import utils, constants

def fetch_bin(url):
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

modes = {}

def human_genome():
    import gzip
    base = "http://hgdownload.cse.ucsc.edu/goldenpath/hg19/chromosomes/chr{}.fa.gz"

    links = {}
    for i in range(1, 23):
        links[f"chr{i}.dna"] = base.format(i)
    links["chrX.dna"] = base.format("X")
    links["chrY.dna"] = base.format("Y")

    for fn, link in links.items():
        print(f"Downloading {fn}...")
        data = fetch_bin(link)

        print(f"Decompressing {fn}...")
        data = gzip.decompress(data)

        print(f"Stripping {fn}...")
        data = utils.strip_fasta(data.decode())

        with open(fn, "w") as file:
            file.write(data)
modes["human-genome"] = {"func": human_genome, "desc": "Downloads all human chromosomes"}

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
