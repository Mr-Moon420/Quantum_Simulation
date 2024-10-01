import math

class Complex_Number:

    real = 0
    imaginary = 0

    def __init__(self, _real, _imaginary):
        global real
        global imaginary

        self.real = _real
        self.imaginary = _imaginary

    def setValue(self, _real, _imaginary):
        global real
        global imaginary

        self.real = _real
        self.imaginary = _imaginary

    def printValue(self):
        print(self.real , " + " , self.imaginary , "i")

    def amplitude(self):
        global real
        global imaginary
        amp = math.sqrt(self.real*self.real + self.imaginary*self.imaginary)
        return amp
    
    def normalize(self):
        global real
        global imaginary

        amp = math.sqrt(self.real*self.real + self.imaginary*self.imaginary)

        real = self.real/amp
        imaginary = self.imaginary/amp

    def toString(self):
        strr = f"{self.real} + {self.imaginary}i"
        return strr
    
    def __mul__(self, value):
        _real = self.real*value.real - self.imaginary*value.imaginary
        _imaginary = self.imaginary*value.real + self.real*value.imaginary

        return Complex_Number(_real, _imaginary)
    
    def __truediv__(self, value):
        res = self * value.conjugate()
        amp = value.amplitude()*value.amplitude()
        res = res * Complex_Number(1/amp, 0)
        return res
    
    def __add__(self,value):
        _real = self.real + value.real
        _imaginary = self.imaginary + value.imaginary

        return Complex_Number(_real, _imaginary)
    
    def __eq__(self, value):
        if self.real == value.real and self.imaginary == value.imaginary:
            return True
        else:
            return False
        
    def conjugate(self):
        self.imaginary = self.imaginary * -1
        return Complex_Number(self.real, self.imaginary)
    
    def zeroNum():
        return Complex_Number(0,0)

    