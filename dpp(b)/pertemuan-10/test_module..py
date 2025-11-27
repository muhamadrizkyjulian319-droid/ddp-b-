import os, sys, math, datetime, hitung2 as h
from hitung2 import *

print(sys.copyright)

def pangkat(x,y):
    return (x**y)
print(pangkat(2,3))

print(math.sin(0.5))
print(math.pow(2,3))
print(math.sqrt(100))
print(math.ceil(0.9))
print(math.factorial(10))

print(datetime.datetime.now())

print(f"jadi hasilnya adalah {h.kurang(3,2)}")
print(f"jadi hasilnya adalah {h.bagi(10,2)}")
print(f"jadi hasilnya adalah {tambah(10,2)}")