import numpy as np
import math
from QuantumSystem import QSys
from QuantumSystem import HSpace

HiblSpace = HSpace(['u','d'])

spinSys = QSys(HiblSpace, np.array([
                                    [0],
                                    [1]
                                    ]))

spinZ = np.array([[1,0],
                  [0,-1]])

spinSys.collapsePermanent()