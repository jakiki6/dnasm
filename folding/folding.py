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

    def fold(self):
        # todo
        pass

    def plot(self):
        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import Axes3D

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_xticks(range(0, self.space.shape[0]))
        ax.set_yticks(range(0, self.space.shape[1]))
        ax.set_zticks(range(0, self.space.shape[2]))
        lx, ly, lz = None, None, None

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
                        if lx != None:
                            ax.plot([lz, z], [lx, x], zs=[-ly, -y], color=(0.7, 0.7, 0.7))
                        lx, ly, lz = x, y, z
        plt.axis('off')
        plt.show()
