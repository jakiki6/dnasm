import hashlib, os

def get_full_object(cid):
    obj = load_object(cid)
    if obj["type"] == "data":
        return obj["data"]
    elif obj["type"] == "link":
        s = b""
        for cid in obj["links"]:
            s += load_object(cid)
        return s

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
    try:
        cwd = os.getcwd()
        home = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "database")
        os.chdir(home)
        with open(cid, "rb") as file:
            data = file.read()
        os.chdir(cwd)
        assert hash_object(data) == cid
        return data
    except:
        raise Exception(f"object {cid} not found")

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
