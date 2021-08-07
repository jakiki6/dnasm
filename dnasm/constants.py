ACIDS = {
    "Ala": ["gct", "gcc", "gca", "gcg"],
    "Arg": ["cgt", "cgc", "cga", "cgg"],
    "Asn": ["aat", "aac"],
    "Asp": ["gat", "gac"],
    "Cys": ["tgt", "tgc"],
    "Gln": ["caa", "cag"],
    "Glu": ["gaa", "gag"],
    "Gly": ["ggt", "ggc", "gga", "ggg"],
    "His": ["cat", "cac"],
    "Ile": ["att", "atc", "ata"],
    "Leu": ["ctt", "ctc", "cta", "ctg"],
    "Lys": ["aaa", "aag"],
    "Met": ["atg"],
    "Phe": ["ttt", "ttc"],
    "Pro": ["cct", "ccc", "cca", "ccg"],
    "Ser": ["tct", "tcc", "tca", "tcg"],
    "Thr": ["act", "acc", "aca", "acg"],
    "Trp": ["tgg"],
    "Tyr": ["tat", "tac"],
    "Val": ["gtt", "gtc", "gta", "gtg"],
    "End": ["taa", "tag", "tga"],
    "Start": ["atg"]
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
