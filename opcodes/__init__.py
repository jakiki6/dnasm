from . import basic

OPCODES = {
    "bases": basic.bases,
    "start": basic.start,
    "end": basic.end,
    "acids": basic.acids,
    "nop": lambda x: "",
}
