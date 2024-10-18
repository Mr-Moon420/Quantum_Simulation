from QuantumSystem import HSpace
from QuantumSystem import QSys
import numpy as np

map = np.array([

    ['.', '.', '.', '.'],
    ['.', '.', '.', '.'],
    ['.', '.', '.', '.'],
    ['.', '.', '.', '.']

])

vecs = []
amps = np.array([ [0] ] * 16)
count = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        vecs.append(f'{i},{j}')

        if i == j:
            amps[count][0] = 1
        else:
            amps[count][0] = 0

        count += 1

HS = HSpace(vecs)
Particle = QSys(HS, amps)
Particle.collapsePermanent()
Particle.printState()

count = 0

for i  in range(len(map)):
    for j in range(len(map[i])):
        if Particle.amplitudes[count][0] == 1:
            print("*",end=" ")
        else:
            print("/", end=" ")

        count += 1
    print("\n")

