import numpy as np, random, math

def fold(acids):
    # make a virtual space for folding
    size = len(acids) + 4
    size -= size % 2
    size += 1
    space = np.zeros((size, size, size))

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

def plot(space):
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xticks(range(0, space.shape[0]))
    ax.set_yticks(range(0, space.shape[0]))
    ax.set_zticks(range(0, space.shape[0]))
    for x in range(0, len(space)):
        for y in range(0, len(space[x])):
            for z in range(0, len(space[x, y])):
                t = space[x, y, z]
                if t > 0:
                    rng = random.Random()
                    rng.seed(t)
                    c = []
                    for i in range(0, 3):
                        c.append(rng.randint(0, 256) / 256)
                    ax.scatter(z, x, -y, zdir='z', c=c)
    plt.axis('off')
    plt.show()
