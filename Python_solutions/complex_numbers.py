import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        real_part = self.real + no.real
        comp_part = self.imaginary + no.imaginary
        return Complex(real_part, comp_part)
        
    def __sub__(self, no):
        real_part = self.real - no.real
        comp_part = self.imaginary - no.imaginary
        return Complex(real_part, comp_part)
    
    def __mul__(self, no):
        real_part = self.real * no.real - self.imaginary * no.imaginary
        comp_part = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real_part, comp_part)
    
    def __truediv__(self, no):
        conj_z2 = (no.real, -no.imaginary)
        numerator_real = self.real * conj_z2[0] - self.imaginary * conj_z2[1]
        numerator_imag = self.real * conj_z2[1] + self.imaginary * conj_z2[0]
        denominator = no.real * no.real + no.imaginary * no.imaginary
        real_part = numerator_real / denominator
        comp_part = numerator_imag / denominator
        return Complex(real_part, comp_part)
    
    def mod(self):
        m1 = math.sqrt((self.real**2 + self.imaginary**2 ))
        return '{:.2f}+0.00i'.format(m1)
    
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
