from math import sqrt, acos, degrees
if __name__ == '__main__':
    AB = int(input())
    BC = int(input())

AC = sqrt(AB**2 + BC**2)
MC = AC/2
# BM = sqrt(BC**2 - MC**2)
angle = round(degrees(acos(BC/AC)))
print('{}\u00b0'.format(angle))
