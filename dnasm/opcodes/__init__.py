from . import basic, protein, database

def run(line, rna):
    if line.opcode in OPCODES.keys():
        return OPCODES[line.opcode](line, rna)
    else:
        raise ValueError(f"Unknown opcode '{line.opcode}'")

OPCODES = {
    "bases": basic.bases,
    "start": basic.start,
    "end": basic.end,
    "acids": basic.acids,
    "nop": lambda x, y: "",
    "protein_db": protein.get_protein_by_id,
    "tail": basic.tail,
    "pad": basic.pad,
    "snippet": database.snippet,
    "cap": basic.cap,
    "linker": basic.linker,
    "compressed": basic.compressed,
    "align": basic.align,
    "point": lambda x, y: ""
}
