import sys, os, requests, random, re, math, json
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "lib"))
import database, utils, constants

def require(num, usage):
    if len(sys.argv) - 2 != num:
        print(sys.argv[0], sys.argv[1], usage)
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
modes["build-snippet"] = {"func": build_snippet, "desc": "Builds rna into the snippet format"}

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
modes["partition-genome"] = {"func": partition_genome, "desc": "Tool to split huge genome into sections and label them"}

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
                char = random.choice("atcg")
            mdata += char
    elif mode == "safe":
        for i in range(0, len(data), 3):
            trip = data[i:i+2]
            if random.randint(0, 99) < ratio:
                for key, val in constants.ACIDS.items():
                    if trip in val:
                        trip = random.choice(val)
            mdata += trip
    else:
        print("Invalid mode!")
        return

    with open(filename, "w") as file:
        file.write(mdata)

modes["mutate-genome"] = {"func": mutate_genome, "desc": "Randomly mutate genome by given ratio (e.g 2.0 for 2%)\nModes:\n\tnatural: randomly mutates\n\tsafe: the built protein stays the same"}

def find_promoter_bacteria():
    filename, = require(1, "<file>")

    # https://www.amberbiology.com/blog/2018/5/20/python-for-genomics-and-next-generation-sequencing
    promoter = 'ttgaca.{15, 25}tataat'

    try:
        with open(filename, "r") as file:
            nmatches = 0

            for match in re.finditer(promoter, file.read().lower().replace("\n", "")):
                nmatches += 1
                print(f"{match.start()} {match.end()} {match.group()}")

            print(f"{nmatches} matches")
    except FileNotFoundError:
        print(f"Not a file!")
modes["find-promoter-bacteria"] = {"func": find_promoter_bacteria, "desc": "Finds promoter from bacteria for potential genes"}

def generate_random_dna():
    try:
        for i in range(0, int(require(1, "<amount>")[0])):
            print(random.choice("atcg"), end="")
    except ValueError:
        print("Not a valid amount", file=sys.stderr)
modes["generate-random-dna"] = {"func": generate_random_dna, "desc": "generates random dna"}

def dump_utrs():
    filename, = require(1, "<file>")

    with open(filename, "r") as file:
        stage = 0
        ptr = 0
        fcontent = file.read()

        utr5 = ""
        content = ""
        utr3 = ""
        tail = 0

        while ptr < len(fcontent):
            if stage == 0:
                utr5 += fcontent[ptr]
                ptr += 1
                if len(utr5) >= 3:
                    if utr5.endswith("atg"):
                        stage = 1
                        utr5 = utr5[:-3]
                        content += "atg"
            if stage == 1:
                if (ptr + 3) >= len(fcontent):
                    print("Unaligned pair in content part!")
                    return
                pair = fcontent[ptr:ptr+3]
                ptr += 3
                content += pair
                if pair in ("tag", "tga", "taa"):
                    stage = 2
            elif stage == 2:
                utr3 += fcontent[ptr]
                ptr += 1

        while utr3[-1] == "a":
            utr3 = utr3[:-1]
            tail += 1

        print(f"utr5: {utr5}\ncontent: {content}\nutr3: {utr3}\ntail is {tail} A(s) long")
modes["dump-utr"] = {"func": dump_utrs, "desc": "Dump utrs and content of mrna"}

def find_starts():
    filename, = require(1, "<file>")

    with open(filename, "r") as file:
        ptr = 3
        content = file.read()

        while ptr < len(content):
            if content[ptr-3:ptr] == "atg":
                print(f"Start found at {ptr}")
            elif content[ptr-3:ptr] in ("tag", "tga", "taa"):
                print(f"Stop found at {ptr}")

            ptr += 1
modes["find-starts"] = {"func": find_starts, "desc": "Find starts and stops in raw material"}

def huge_format():
    infn, outfn = require(2, "<input file> <output file>")

    with open(infn, "r") as infile:
        with open(outfn, "w") as outfile:
            char = " "

            while char != "":
                char = infile.read(1).lower().replace("u", "t").replace("n", "a")

                if char in "atcg":
                    outfile.write(char)
modes["huge-format"] = {"func": huge_format, "desc": "Format a huge file (like the human genome)"}

def decompress_iupac():
    infn, outfn = require(2, "<input file> <output file>")

    with open(infn, "r") as infile:
        with open(outfn, "w") as outfile:
            char = " "

            while char != "":
                char = infile.read(1)

                if char in constants.IUPAC.keys():
                    outfile.write(constants.IUPAC[char][0])
modes["decompress-iupac"] = {"func": decompress_iupac, "desc": "Decompress protein code from IUPAC to raw"}

def compress_iupac():
    infn, outfn = require(2, "<input file> <output file>")

    index = {}
    for key, val in constants.IUPAC.items():
        for v in val:
            index[v] = key

    with open(infn, "r") as infile:
        with open(outfn, "w") as outfile: 
            pair = " "

            while pair != "":
                pair = ""
                while len(pair) < 3:
                    char = infile.read(1).lower()

                    if char == "":
                        break

                    if char in "atcg":
                        pair += char

                try:
                    outfile.write(index[pair])
                except KeyError:
                    outfile.write(pair)
modes["compress-iupac"] = {"func": compress_iupac, "desc": "Compress protein code from raw to IUPAC"}

def sign_dna():
    infn, outfn, keyfn = require(3, "<input file> <output file> <sign data>")

    with open(keyfn, "rb") as file:
        k = 0
        for i in file.read():
            k = (k << 8) | i

    with open(infn, "r") as file:
        content = file.read()
        scontent = ""

    for i in range(0, len(content), 3):
        pair = content[i:i+3]

        for key, val in constants.ACIDS.items():
            if pair in val:
                j = k % len(val)
                k //= len(val)

                scontent += val[j]

                break

    if k > 0:
        print(f"Signature data is too large! {math.ceil(math.log(k, 256))} byte(s) too much")
        exit(1)

    with open(outfn, "w") as file:
        file.write(scontent)
modes["sign-dna"] = {"func": sign_dna, "desc": "Apply signature to dna"}

def read_signature():
    infn, outfn = require(2, "<input file> <output file>")

    with open(infn, "r") as file:
        content = file.read()
        k = 0
        shift = 1

    for i in range(0, len(content), 3):
        pair = content[i:i+3]

        for key, val in constants.ACIDS.items():
            if pair in val:
                k = k + (shift * val.index(pair))
                shift *= len(val)

                break

    rcontent = k.to_bytes(math.ceil(k.bit_length() / 8), "big")

    with open(outfn, "wb") as file:
        file.write(rcontent)
modes["read-signature"] = {"func": read_signature, "desc": "Reads signature applied with sign-dna"}

def find_paddings():
    infn, _minl = require(2, "<input file> <minimal length>")
    minl = int(_minl)

    with open(infn, "r") as infile:
        char = " "
        streak = 0
        regions = []
        ptr = 0

        while char != "":
            char = infile.read(1)

            if char.lower() == "a":
                streak += 1
            elif char.lower() in "tcg":
                if streak >= minl:
                    regions.append({
                        "start": ptr - streak - 1,
                        "end": ptr - 1,
                        "length": streak
                    })

                streak = 0

            ptr += 1

        print(sorted(regions, key=lambda k: k["length"]))

modes["find-paddings"] = {"func": find_paddings, "desc": "Find 'a' paddings in a huge file"}

def find_pattern():
    pfn, infn = require(2, "<pattern filename> <input file>")

    with open(pfn, "r") as pfile:
        pattern = ""
        for char in pfile.read():
            if char in "atcg":
                pattern += char
        streak = 0
        index = 0

    with open(infn, "r") as infile:
        char = " "

        while char != "":
            char = infile.read(1)

            if char == pattern[streak]:
                streak += 1

                if streak == len(pattern):
                    print(index)
                    streak = 0
                    index += len(pattern)
            else:
                streak = 0
                index += 1
modes["find-pattern"] = {"func": find_pattern, "desc": "Find specific pattern in huge file"}

def collect_stats():
    infn, = require(1, "<input file>")

    with open(infn, "r") as infile:
        stats = {
            "bases": {
                "a": 0,
                "t": 0,
                "c": 0,
                "g": 0
            }
        }

        while True:
            char = infile.read(1).lower()

            if char == "":
                break

            if not char in "atcg":
                continue

            stats["bases"][char] += 1

    print(json.dumps(stats, indent=4))
modes["collect-stats"] = {"func": collect_stats, "desc": "Collect statistics of dna"}

def compress():
    infn, outfn = require(2, "<input file> <output file>")

    with open(infn, "r") as inf:
        with open(outfn, "wb") as outf:
            b = 0
            read = 0
    
            while True:
                char = inf.read(1)
                if not char in "atcg":
                    continue
                if char == "":
                    if read != 0:
                        outf.write(bytes([b << (2 * (4 - read))]))
                    break
                    

                b <<= 2
                b |= constants.MAPPING[char]
                read += 1

                if read == 4:
                    outf.write(bytes([b]))

                    b = 0
                    read = 0
modes["compress"] = {"func": compress, "desc": "Compress dna"}

def decompress():
    infn, outfn = require(2, "<input file> <output file>")

    with open(infn, "rb") as inf:
        with open(outfn, "w") as outf:
            while True:
                char = inf.read(1)
                if char == b"":
                    break
                b = char[0]

                s = ""
                for i in range(0, 4):
                    s += constants.RMAPPING[b & 0b11]
                    b >>= 2

                outf.write(s[::-1])
modes["decompress"] = {"func": decompress, "desc": "Decompress dna"}

def complement():
    infn, outfn = require(2, "<input file> <output file>")

    with open(infn, "r") as inf:
        with open(outfn, "w") as outf:
            while True:
                char = inf.read(1).lower().strip()
                if char == "":
                    break

                if not char in "atcg":
                    continue

                outf.write(constants.COMPLEMENT[char])
modes["complement"] = {"func": complement, "desc": "Convert dna into its complement form"}

def analyse_entropy():
    infn, mode = require(2, "<input file> <mode>")

    if not mode in ("g", "graph", "c", "console", "r", "raw"):
        print("Not a valid mode: specify one of 'graph', 'console' or 'raw' or their first letter")
        return

    entropies = []
    with open(infn, "r") as infile:
        infile.seek(0, 2)
        chunk_size = infile.tell() // 1024
        infile.seek(0)

        while True:
            chunk = infile.read(chunk_size)
            if len(chunk) == 0:
                break

            entropy = utils.get_entropy(chunk)
            entropies.append(entropy)

    if mode in ("g", "graph"):
        import matplotlib.pyplot as plt

        plt.plot(entropies)
        plt.show()
    elif mode in ("c", "console"):
        size = os.get_terminal_size().columns
        bar_size = os.get_terminal_size().lines - 5
        entropies = utils.resize(entropies, size)
        heights = [[] for _ in range(0, bar_size)]

        for i in range(0, len(entropies)):
            h = math.floor(entropies[i] * bar_size)

            while h:
                heights[h].append(i)
                h -= 1

        for hs in heights[::-1]:
            line = [" " for _ in range(0, size)]

            for h in hs:
                line[h] = "#"

            print("".join(line))
    elif mode in ("r", "raw"):
        print(entropies)
            
modes["analyse-entropy"] = {"func": analyse_entropy, "desc": "Analyse the entropy of dna"}
