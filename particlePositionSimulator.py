from Eigenvector import Eigenstate
from Complex_Num import Complex_Number as CN
from QuantumSystem import QSys

vecs = []
asc = 97

def prefSys(num):
    arr1 = [2,3,5,9,8,12,14,15]
    arr2 = [6,7,10,11]
    if num in arr1:
        return CN(2,0)
    elif num in arr2:
        return CN(0,0)
    else:
        return CN(1/2,0)

for i in range(16):
    basis = Eigenstate.fromCompNum(prefSys(asc-96), chr(asc))
    asc += 1
    vecs.append(basis)

particle = QSys(vecs)
particle.normalize()

map = [ [ ['a', '/'], ['b', '/'], ['c', '/'], ['d', '/']] , [ ['e', '/'], ['f', '/'], ['g', '/'], ['h', '/']], [ ['i', '/'], ['j', '/'], ['k', '/'], ['l', '/']], [ ['m', '/'], ['n', '/'], ['o', '/'], ['p', '/']] ]
mapOut = [ [ ['a', 0], ['b', 0], ['c', 0], ['d', 0]] , [ ['e', 0], ['f', 0], ['g', 0], ['h', 0]], [ ['i', 0], ['j', 0], ['k', 0], ['l', 0]], [ ['m', 0], ['n', 0], ['o', 0], ['p', 0]] ]

def resetMap():
    for i in map:
        for j in i:
            j[1] = '/'

def sim():
    state = particle.collapse()

    for i in map:
        for j in i:
            if j[0] == state:
                j[1] = '*'

    for i in map:
        for j in i:
            if j[1] == '*':
                mapOut[map.index(i)][i.index(j)][1] += 1

    resetMap()

for i in range(1000):
    sim()

for i in mapOut:
    for j in i:
        if i.index(j) != len(i) -1:
            print(j[1], end='-')
        else:
            print(j[1])