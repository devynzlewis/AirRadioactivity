import numpy as np
import matplotlib.pyplot as plt

file = open('Ba-133-Feb11Data.txt', 'r' )


nValues = int(file.readline())

print(nValues)

values = np.empty((nValues + 2,2))

i = 0

while True:
    line = int(file.readline())

    values[i,0] = i
    values[i,1] = line

    if not line:
        break

    i += 1

print(np.shape(values))

plt.xlim(0,4100)
plt.yscale('log')
plt.plot(values[:,0], values[:,1])

plt.show()

