from Complex_Num import Complex_Number

class Eigenstate:

    comp_num = 0
    symbol = 'a'

    def __init__(self, _real, _imaginary, _symbol):
        self.symbol = _symbol
        self.comp_num = Complex_Number(_real, _imaginary)

    @classmethod
    def fromCompNum(self, _comp_num, _symbol):
        res = Eigenstate(_comp_num.real, _comp_num.imaginary, _symbol)
        return res