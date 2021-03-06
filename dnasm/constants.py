ACIDS = {
    "Ala": "gct",
    "Arg": "cgt",
    "Asn": "aat",
    "Asp": "gat",
    "Cys": "tgt",
    "Gln": "caa",
    "Glu": "gaa",
    "Gly": "ggt",
    "His": "cat",
    "Start": "atg",
    "Ile": "att",
    "Leu": "ctt",
    "Lys": "aaa",
    "Met": "atg",
    "Phe": "ttt",
    "Pro": "cct",
    "Ser": "tct",
    "Thr": "act",
    "Trp": "tgg",
    "Tyr": "tat",
    "Val": "gtt",
    "End": "taa",
}

IUPAC = {
    "A": "gct",
    "B": "gat",
    "C": "tgt",
    "D": "gat",
    "E": "gaa",
    "F": "ttt",
    "G": "ggt",
    "H": "cat",
    "I": "att",
    "K": "aaa",
    "L": "tta",
    "M": "atg", # start
    "N": "cgt",
    "O": "tag", # can be decoded as stop
    "P": "cct",
    "Q": "caa",
    "R": "aga",
    "S": "tct",
    "T": "act",
    "U": "tga", # can be decoded as stop
    "V": "gtt",
    "W": "tgg",
    "Y": "tat",
    "Z": "gaa",
    "J": "ctt",
    "X": "aaa",
    "*": "taa", # safe stop since it will be decoded as stop by all cells
    "-": "",
}

MAPPING = {
    "t": 0b00,
    "c": 0b01,
    "a": 0b10,
    "g": 0b11,
    "u": 0b00,
}
