import hashlib, os

def snippet(line, content):
    cid = line.replace("snippet", "")

    return resolve(cid)

def resolve(cid):
    obj = get_object(cid)
    if obj["type"] == "link":
        print(f"found nested object {cid}")
        s = ""
        for link in obj["data"]:
            s += resolve(link)
        return s
    elif obj["type"] == "data":
        return obj["data"]
    else:
        return ""

def get_object(cid):
    obj = get_raw_object(cid)
    if obj[0] == 0x00:
        return {
            "type": "data",
            "data": obj[1:].decode("utf8")
        }
    elif obj[1] == 0x01:
        data = obj[1:]
        hashlength = int.from_bytes(data[:4], "big")
        data = data[4:]

        assert len(data) % hashlength == 0, f"link object {cid} is corrupted"

        hashes = []
        for i in range(0, len(data), hashlength):
            hashes.append(base64.b64encode(data[i:i+hashlength]).decode())

        return {
            "type": "link",
            "data": hashes
        }

def get_raw_object(cid):
    pwd = os.getcwd()
    home = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))), "database")
    os.chdir(home)

    if os.path.isfile(cid):
        with open(cid, "rb") as file:
            data = file.read()
            os.chdir(pwd)
        assert verify(data, cid), f"hash doesn't match for {cid}"
        return data

    raise Exception(f"{cid} not found")

def verify(data, cid):
    if cid[0:2] == "00":
        hash = "00" + hashlib.sha256(data).hexdigest()
        return cid == hash
    return False
