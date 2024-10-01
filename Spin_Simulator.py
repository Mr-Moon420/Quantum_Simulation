from Complex_Num import Complex_Number
from Eigenvector import Eigenstate
from QuantumSystem import QSys
import random
import math


spinSys = QSys([Eigenstate(math.sqrt(2/3),0,'u'),Eigenstate(math.sqrt(1/3),0,'d')])
spinSys.normalize()

print(spinSys.prob('u'))