import hashlib, os, requests

sources = [
    f"file://{os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'database')}",
    "file:///usr/share/dnasm/database",
    "https://raw.githubusercontent.com/jakiki6/dnasm-database/main/"
]

def get_full_object(cid):
    obj = load_object(cid)

    if obj["type"] == "data":
        return obj["data"]
    elif obj["type"] == "link":
        s = b""
        for cid in obj["links"]:
            s += load_object(cid)
        return s
    else:
        return ""

def build_data_object(data):
    data = b"\x00" + data
    return data

def build_link_object(cids):
    data = b"\x01"
    for cid in cids:
        data += cid.encode() + "\x00"
    return data

def build_meta_object(data):
    data = b"\x02" + data
    return data

def hash_object(data):
    return "00" + hashlib.sha256(data).hexdigest()

def save_raw_object(data):
    hash = hash_object(data)

    cwd = os.getcwd()
    home = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "database")
    os.chdir(home)
    with open(hash, "wb") as file:
        file.write(data)
    os.chdir(cwd)

    return os.path.join(home, hash)

def load_raw_object(cid):
    for source in sources:
        data = load_data_from(cid, source)
        if data != None:
            return data
    msg = f"{cid} not found in database\n"
    msg += "searched sources:\n"

    for source in sources:
        msg += f"\t{source} -> not found\n"

    raise Exception(msg)

def load_data_from(cid, source):
    try:
        if source.startswith("file://"):
            source = source[7:]
            cwd = os.getcwd()
            os.chdir(source)
            with open(cid, "rb") as file:
                data = file.read()
            os.chdir(cwd)
            assert hash_object(data) == cid
            return data
        elif source.startswith("http://") or source.startswith("https://"):
            source = source + "/" + cid
            data = requests.get(source).content
            if data == b'404: Not Found':
                data = None
            return data
    except Exception:
        return None

def load_object(cid):
    obj = load_raw_object(cid)

    if obj[0] == 0x00:
        return {
            "type": "data",
            "data": obj[1:]
        }
    elif obj[0] == 0x01:
        cids = []
        for cid in obj[1:].split(b"\x00"):
            if cid != b"":
                cids.append(cid.decode())

        return {
            "type": "link",
            "links": cids
        }
    elif obj[0] == 0x03:
        return {
            "type": "meta",
            "data": obj[1:]
        }
    else:
        return {
            "type": "unknown",
            "data": obj
        }
