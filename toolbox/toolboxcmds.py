import hashlib, os

modes = {}

def nop(file):
    pass
modes["nop"] = {"func": nop, "desc": "No operation\nJust for testing"}

def build_snippet(file):
    with open(file, "rb") as f:
        data = f.read()
    data = b"\x00" + data
    hash = "00" + hashlib.sha256(data).hexdigest()
    print(f"Building snippet object {hash}")

    home = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "database")
    os.chdir(home)

    with open(hash, "wb") as file:
        file.write(data)
modes["build_snippet"] = {"func": build_snippet, "desc": "Builds rna into the snippet format"}
