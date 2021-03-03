def shift_line(data, num):
    for i in range(0, num):
        data.opcode = data.args[0]
        data.args.pop(0)
    return data

def req_int(string):
    try:
        return int(string)
    except:
        print(f"{string} is not a valid number")
