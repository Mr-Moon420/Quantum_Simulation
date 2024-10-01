from Eigenvector import Eigenstate
from Complex_Num import Complex_Number
from QuantumSystem import QSys

f = open('map.txt', 'r')

mapStr = f.readlines()

mapVal = [ ]

print(mapStr)

for i in mapStr:
    j = i.split("-")
    j[3].removesuffix('\n')

    mapVal.append(j)

asc = 97
vec = []

for i in mapVal:
    for j in i:
        basis = Eigenstate.fromCompNum(Complex_Number(j, 0), chr(asc))
        asc += 1
        vec.append(basis)

state = QSys(vec)
state.normalize()

state.printState()