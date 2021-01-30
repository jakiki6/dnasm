def tabs2dict(buf):
    _buf = buf.split("\n")
    buf = []
    for line in buf:
        if line.strip() != "":
            buf.append(line)
    del _buf
    level = 0
    data_stack = []
    name_stack = []
    data = {}

    for line in buf:
        clevel = get_level(line)
        # todo

def get_level(line):
    level = 0
    for char in line:
        if char == " ":
            level += 1
        else:
            break
    return level
