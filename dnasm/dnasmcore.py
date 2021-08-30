import sys
import utils, opcodes

class OpCode(object):
    def __init__(self, opcode, args, line):
        self.opcode = opcode
        self.args = args
        self.line = line
    def __str__(self):
        return f"OpCode(opcode='{self.opcode}', args={self.args})"
    def __repr__(self):
        return self.__str__()

def replace_whitespaces(line):
    nline = ""
    hit = False
    for char in line:
        if char in " \t,":
            if not hit:
                nline += " "
                hit = True
            continue
        else:
            hit = False
            nline += char
    return nline

def parse(text):
    opcodes = []
    lline = ""
    is_escape = False
    lindex = 0
    for line in text.split("\n"):
        lindex += 1
        if is_escape:
            line = lline + line
            is_escape = False
        line = line.strip()
        line = line.split(";")[0].strip()
        line = replace_whitespaces(line)
        if len(line) == 0:
            continue
        if line[-1] == "\\":
            is_escape = True
            lline = line[:-1]
        else:
            line = line.split(" ")
            data = OpCode(line[0], line[1:], lindex)
            opcodes.append(data)
    return opcodes

def merge(data):
    for index, line in enumerate(data):
        if line.opcode == "%include":
            try:
                with open(line.args[0], "r") as file:
                    for nline in parse(file.read()):
                        data.insert(index, nline)
                        index += 1
                    data.remove(line)
                    merge(data)
                    break
            except:
                print(f"Cannot open file {line.args[0]}", file=sys.stderr)

def preprocess(data):
    for index, line in enumerate(data):
        try:
            if line.opcode == "times":
                num = utils.req_int(line.args[0])
                nline = utils.shift_line(line, 2)
                for i in range(0, num):
                    data.insert(index, nline)
                data.remove(line)
                preprocess(data)
                break
        except Exception as e:
            print(f"error in line {line.line}: {e}")
            sys.exit(1)

def run(data):
    rna = ""
    for line in data:
        try:
            rna += opcodes.run(line, rna)
        except Exception as e:
            print(f"error in line {line.line}: {e}")
            sys.exit(1)
    return rna

def process(text):
    data = parse(text)
    merge(data)
    preprocess(data)
    rna = run(data) 
    return rna
