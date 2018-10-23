import random
from fractions import gcd
from math import sqrt; from itertools import count, islice

def lucaslemer(prime):
    S,k,M = 4,1,2**prime-1
    while k!=(prime-1):
        S = ((S*S)-2)%M
        k+=1
    if S == 0: return True
    else: return False

def randomprime():
    while True:
    	prime = random.randint(32,1024)
    	if (2 in [prime,2**prime%prime]):
    		if lucaslemer(prime): break
    return (2**prime-1, random.randint(3,13))

def randedge(a,b):
	return random.randint(a+1,b-1)

def egcd(a, b):
    if a == 0: return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1: raise Exception("Error")
    else: return x % m

def randomk(p):
    k = random.randint(2,p-1)
    if (gcd(k,p-1)!=1): return randomk(p)
    else: return (k, modinv(k,p-1))
