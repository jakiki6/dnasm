from . import basic, protein, database

OPCODES = {
    "bases": basic.bases,
    "start": basic.start,
    "end": basic.end,
    "acids": basic.acids,
    "nop": lambda x, y: "",
    "protein_db": protein.get_protein_by_id,
    "tail": basic.tail,
    "point": basic.point,
    "pad": basic.pad,
    "snippet": database.snippet,
    "cap": basic.cap,
    "linker": basic.linker,
    "iupac": basic.iupac,
}
