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
    "Stop": ["taa", "tag", "tga"],
    "Start": ["atg"],
    "Any": ["nnn"]
}

IUPAC = {
    "A": ACIDS["Ala"],
    "B": ACIDS["Asp"] + ACIDS["Asn"],
    "C": ACIDS["Cys"],
    "D": ACIDS["Asp"],
    "E": ACIDS["Glu"],
    "F": ACIDS["Phe"],
    "G": ACIDS["Gly"],
    "H": ACIDS["His"],
    "I": ACIDS["Ile"],
    "K": ACIDS["Lys"],
    "L": ACIDS["Leu"],
    "M": ACIDS["Start"],
    "N": ACIDS["Asn"],
    "O": ["tag"],
    "P": ACIDS["Pro"],
    "Q": ACIDS["Gln"],
    "R": ACIDS["Arg"],
    "S": ACIDS["Ser"],
    "T": ACIDS["Thr"],
    "U": ["tga"],
    "V": ACIDS["Val"],
    "W": ACIDS["Trp"],
    "Y": ACIDS["Tyr"],
    "Z": ACIDS["Glu"] + ACIDS["Gln"],
    "J": ACIDS["Leu"],
    "X": ACIDS["Any"],
    "*": ACIDS["Stop"],
    "-": [""],
    ".": [""]
}

MAPPING = {
    "a": 0b00,
    "c": 0b01,
    "t": 0b10,
    "n": 0b10,
    "g": 0b11,
    "u": 0b00,
    "": 0b00,
}

RMAPPING = {
    0b00: "a",
    0b01: "c",
    0b10: "t",
    0b11: "g"
}
