'''
Find the next perfect square!
7kyu
7 d ago
'''
from math import sqrt
import math

def find_next_square(sq):
    x=sqrt(sq)
    y=int(x)
    if (math.isclose(x,y,abs_tol=0.0)):
        return int((x+1)**2)
    else:
        return -1
