rom fractions import Fraction
from functools import reduce

def product(fracs):
    num_ls = [i.numerator for i in fracs]
    den_ls = [i.denominator for i in fracs]
    t = Fraction(reduce(lambda x,y:x*y, num_ls),reduce(lambda x,y:x*y,den_ls))
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
