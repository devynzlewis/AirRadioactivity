import numpy as np
import matplotlib.pyplot as plt

file = open('Ba-133-Feb11Data.txt', 'r' )


nValues = int(file.readline())

print(nValues)

values = np.empty((nValues + 1,2))

i = 0

while True:
    line = file.readline()

    values[i,0] = i
    values[i,1] = int(line)

    if not line:
        break

    i += 1

print(values[0,0])
print('hello world')