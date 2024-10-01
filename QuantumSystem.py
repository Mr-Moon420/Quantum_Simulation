from Eigenvector import Eigenstate
import random
import math
from Complex_Num import Complex_Number

class HSpace:
    eigenVecs = []

    def __init__(self, vecs):
        self.eigenVecs = vecs

class QSys:
    basis_vectors= []
    hspace = HSpace([])

    def __init__(self, stateList, space):
        self.basis_vectors = stateList
        self.hspace = space

        #adding Unadded Components
        for i in self.hspace.eigenVecs:
            added = False
            for j in self.basis_vectors:
                if j.symbol == i:
                    added = True
                    break

            if added == False:
                self.basis_vectors.append(Eigenstate(0,0,i))

        #sorting
        for i in range(len(self.hspace.eigenVecs)):
            for j in range(len(self.basis_vectors)):
                if self.basis_vectors[j].symbol == self.hspace.eigenVecs[i]:
                    temp = self.basis_vectors[i]
                    self.basis_vectors[i] = self.basis_vectors[j]
                    self.basis_vectors[j] = temp
                    break

    def printState(self):
        for i in self.basis_vectors:
            print(f"({i.comp_num.toString()})|{i.symbol}> + ", end='')
        print(' ')

    def collapse(self):
        _weights = []

        for i in self.basis_vectors:
            _weights.append(i.comp_num.amplitude())
            #print(i.comp_num.toString())
            #print(i.comp_num.amplitude())

        outcome = random.choices(self.basis_vectors, weights=_weights, k=1)
        return outcome[0].symbol
    
    def collapseSave(self):
        _weights = []

        for i in self.basis_vectors:
            _weights.append(i.comp_num.amplitude())
            #print(i.comp_num.toString())
            #print(i.comp_num.amplitude())

        outcome = random.choices(self.basis_vectors, weights=_weights, k=1)[0]

        for i in self.basis_vectors:
            if i.symbol == outcome.symbol:
                i.comp_num = Complex_Number(1,0)
            else:
                i.comp_num = Complex_Number(0,0)

        return outcome.symbol
    
    def normalize(self):
        amp = 0

        for i in self.basis_vectors:
            amp += (i.comp_num.amplitude())*(i.comp_num.amplitude())

        amp = math.sqrt(amp)

        for i in self.basis_vectors:
            i.comp_num = i.comp_num*(Complex_Number(1/amp, 0))

    def amp(self):
        amp = 0

        for i in self.basis_vectors:
            amp += (i.comp_num.amplitude())*(i.comp_num.amplitude())

    def bra(self):
        conjugate_basis = []

        for i in self.basis_vectors:
            braVec = Eigenstate.fromCompNum(i.comp_num.conjugate(), i.symbol)
            conjugate_basis.append(braVec)

        braRes = QSys(conjugate_basis, self.hspace)
        return braRes
    
    def __mul__(self, other):
        braVec = other.bra()
        res = Complex_Number(0,0)

        for i in self.basis_vectors:
            for j in braVec.basis_vectors:
                if i.symbol == j.symbol:
                    prod = i.comp_num*j.comp_num
                    #prod.printValue()
                    res = res + prod

        return res
    
    def prob(self, _symbol):
        probability = 0
        for i in self.basis_vectors:
            if i.symbol == _symbol:
                probability = i.comp_num.amplitude()*i.comp_num.amplitude()

        return probability
    
    def getComponent(self, vec):
        sys = QSys([Eigenstate.fromCompNum(Complex_Number(1,0), vec)], self.hspace)
        prod = self * sys
        return prod
    
    def nullVec(self):
        res = []
        for i in self.basis_vectors:
            if i.comp_num == Complex_Number(0,0):
                res.append(i.symbol)

        return res
    


class QOperator:
    matrix = [ [] ]
    hspace = HSpace([])

    def __init__(self, _mat, space):
        self.matrix = _mat
        self.hspace = space
    
    def __mul__(self, vec):
        vecs = []

        for i in self.matrix:
            sum = Complex_Number(0,0)
            for j in i:
                prod = j * vec.basis_vectors[i.index(j)].comp_num
                sum = sum + prod
            vecs.append(Eigenstate.fromCompNum(sum, self.hspace.eigenVecs[self.matrix.index(i)]))
        
        resSys = QSys(vecs, self.hspace)
        return resSys
    
    def expectedValue(self, sys):
        vec = self * sys
        res = sys * vec
        return res


