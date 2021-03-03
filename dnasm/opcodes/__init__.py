from . import basic, protein, database

def run(line):
    if line.opcode in OPCODES.keys():
        return OPCODES[line.opcode](line)
    else:
        return ""

OPCODES = {
    "bases": basic.bases,
    "start": basic.start,
    "end": basic.end,
    "acids": basic.acids,
    "nop": lambda x: "",
    "protein_db": protein.get_protein_by_id,
    "tail": basic.tail,
    "pad": basic.pad,
    "snippet": database.snippet,
    "cap": basic.cap,
    "linker": basic.linker,
    "iupac": basic.iupac,
}
