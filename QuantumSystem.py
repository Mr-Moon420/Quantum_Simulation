import numpy as np
import random
import math
from termcolor import colored, cprint

class HSpace:
    eigenVec = []

    def __init__(self, _vecs):
        self.eigenVec = _vecs

class QSys:
    amplitudes = np.array([])
    hspace = HSpace({})

    def __init__(self, _space, amps):
        self.hspace = _space
        self.amplitudes = amps

    def printState(self):
        for i in range(len(self.hspace.eigenVec)):
            print(f"({self.amplitudes[i]})|{self.hspace.eigenVec[i]}> +", end=' ')

    def collapse(self):
        _weights = []

        for i in self.amplitudes:
            prob = i[0]*np.conjugate(i[0])
            _weights.append(prob.real)
        
        outcome = random.choices(self.hspace.eigenVec, weights=_weights, k=1)[0]
        return outcome
    
    def collapsePermanent(self):
        _weights = []

        for i in self.amplitudes:
            prob = i[0]*np.conjugate(i[0])
            _weights.append(prob.real)
        
        outcome = random.choices(self.hspace.eigenVec, weights=_weights, k=1)[0]

        for i in range(len(self.hspace.eigenVec)):
            if self.hspace.eigenVec[i] == outcome:
                self.amplitudes[i][0] = 1 + 0j
            else:
                self.amplitudes[i][0] = 0 + 0j

        return outcome
    
    def normalize(self):
        amp = 0

        for i in self.amplitudes:
            sq = i[0]*np.conjugate(i[0])
            amp += sq

        amp = math.sqrt(amp.real)

        self.amplitudes = self.amplitudes/amp

    def bra(self):
        braMat = np.transpose(self.amplitudes)

        for i in range(len(braMat[0])):
            braMat[0][i] = np.conjugate(braMat[0][i])

        return braMat
    
    def __mul__(self, other):
        bra = other.bra()
        res = np.matmul(bra,self.amplitudes)
        return res[0][0]
    
    def exp(self, operator):
        res = np.matmul(operator, self.amplitudes)
        res = np.matmul(self.bra(), res)

        return res[0][0].real