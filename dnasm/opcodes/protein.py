import sys, requests

import utils, constants

from __main__ import logger

def get_protein_by_id(line, rna):
    protein_id = line.args[0]
    protein = ""

    buf = requests.get(f"https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id={protein_id}&db=protein&report=fasta").content.decode()
    buf = "".join([x for x in buf.split("\n")[1:]])
    buf = buf.strip().replace(" ", "").replace("\t", "")

    for char in buf:
        try:
            protein += constants.IUPAC[char][0]
        except:
            logger.fatal(f"Invalid IUPAC char {char} in protein {protein_id}")

    return protein
