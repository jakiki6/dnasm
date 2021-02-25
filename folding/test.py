import folding
from constants import spike_test
import numpy as np

folder = folding.ShakeFolder(spike_test[:20])

print("Test 1: run it :D")
folder.plot()
folder.fold()

print("Test 2: plot it")
folder.plot()

print("Test 3: show lines")
folder.hhcons = [
        (
            (0, 0, 0),
            (0, 2, 0)
        )
]
folder.acons = [ 
        (
            (1, 0, 0),
            (1, 2, 0)
        )
]
folder.space = np.zeros((len(folder.space), len(folder.space), len(folder.space)))
folder.plot()
