import numpy as np, random, math



class Folder(object):
    def __init__(self, acids):
        self.acids = acids
        # make a virtual space for folding
        size = len(self.acids) + 4
        size -= size % 2
        size += 1
        self.space = np.zeros((size, size, size))

        # fill the space with the actual acids
        # addressing is [x][y][z]

        # y
        # | z
        # |/
        # 0----x
        # the acid chain goes from min middle middle to max middle middle
        middle = math.ceil(size / 2)
        for i in range(2, len(self.acids) + 2):
            self.space[middle][middle][i] = self.acids[i - 2]

        # make a list of amino connections
        self.acons = []
        # make a list of H-H connections
        self.hhcons = []

        # setup acons
        for i in range(2, len(self.acids) + 1):
            self.acons.append(((middle, middle, i), (middle, middle, i + 1)))

    def fold(self):
        raise NotImplementedError("This is a generic class")

    def plot(self):
        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import Axes3D

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_xticks(range(0, self.space.shape[0]))
        ax.set_yticks(range(0, self.space.shape[1]))
        ax.set_zticks(range(0, self.space.shape[2]))

        for x in range(0, len(self.space)):
            for y in range(0, len(self.space[x])):
                for z in range(0, len(self.space[x, y])):
                    t = self.space[x, y, z]
                    if t > 0:
                        rng = random.Random()
                        rng.seed(t)
                        c = []
                        for i in range(0, 3):
                            c.append(rng.randint(0, 256) / 256)
                        ax.scatter(z, x, -y, zdir='z', color=c)

        for acon in self.acons:
            ax.plot([acon[1][2], acon[0][2]], [acon[1][0], acon[0][0]], zs=[-acon[1][1], -acon[0][1]], color=(0.7, 0.7, 0.7))

        for hhcon in self.hhcons:
            ax.plot([hhcon[1][2], hhcon[0][2]], [hhcon[1][0], hhcon[0][0]], zs=[-hhcon[1][1], -hhcon[0][1]], color=(0.7, 0.85, 1))

        plt.axis('off')
        plt.show()

class ShakeFolder(Folder):
    def fold(self):
        pass
