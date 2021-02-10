import numpy as np, random, math

def fold(acids):
    # make a virtual space for folding
    size = len(acids) + 4
    size -= size % 2
    size += 1
    space = np.zeros((size, size, size)).astype(int)

    # fill the space with the actual acids
    # addressing is [x][y][z]

    # y
    # | z
    # |/
    # 0----x
    # the acid chain goes from min middle middle to max middle middle
    middle = math.ceil(size / 2)
    for i in range(2, len(acids) + 2):
        space[middle][middle][i] = acids[i - 2]

    return space
