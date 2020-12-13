from . import basic, protein

OPCODES = {
    "bases": basic.bases,
    "start": basic.start,
    "end": basic.end,
    "acids": basic.acids,
    "nop": lambda x: "",
    "protein_db": protein.get_protein_by_id,
}
