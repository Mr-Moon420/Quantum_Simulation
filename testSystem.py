from Complex_Num import Complex_Number as CN
from Eigenvector import Eigenstate
from QuantumSystem import HSpace
from QuantumSystem import QSys
from QuantumSystem import QOperator
import math

vecs = [Eigenstate.fromCompNum(CN(1/math.sqrt(2),0), 'u'), Eigenstate.fromCompNum(CN(1/math.sqrt(2),0), 'd')]

space = HSpace(['u','d'])
upSys = QSys(vecs, space)
upSys.printState()

spinZ = QOperator([ [ CN(1,0), CN(0,0) ], [ CN(0,0), CN(-1,0) ] ], space)

ex = spinZ.expectedValue(upSys)
ex.printValue()

