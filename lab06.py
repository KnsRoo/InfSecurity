import random, math

def isPrime(n):
	return 2 in [n,2**n%n] 

def randomprime():
	prime = random.randint(1,30000)
	return prime if isPrime(prime) else randomprime()

def gcd(a,b):
    while a != b:
        if a > b: a = a - b
        else: b = b - a
    return a

def p_root(mod):
	rset = set(num for num in range (1, mod) if gcd(num, mod) == 1)
	for g in range(1, mod):
		aset = set(pow(g, powers) % mod for powers in range (1, mod))
		if rset == aset: return g

class Peer():
	def __init__(self,g,p):
		self.g, self.p = g, p
		self.k = random.randint(10,99)
		self.mod = (self.g**self.k)%self.p

	def getsecret(self, R, key = False):
		self.secret = (R**self.k)%p
		if key: self.key = self.secret
			
COUNT = 5 
p = randomprime()
g = p_root(p)
PEERS = [Peer(g,p) for i in range(COUNT)]

names = ['Alisa', 'Bob', 'Carol', 'Melory', 'Ilya','Lera','Inna','Vasya']

for i in range(len(PEERS)):
	if len(PEERS) == 2:
		PEERS[(i+1)%len(PEERS)].getsecret(PEERS[(i)%len(PEERS)].mod, key = True)
	else:
		PEERS[(i+1)%len(PEERS)].getsecret(PEERS[(i)%len(PEERS)].mod)
		j = i+2
		for x in range(len(PEERS)-3):
			PEERS[j%len(PEERS)].getsecret(PEERS[(j-1)%len(PEERS)].secret)
			j+=1
		PEERS[(i+len(PEERS)-1)%len(PEERS)].getsecret(PEERS[(i+len(PEERS)-2)%len(PEERS)].secret, key = True)

for i in range(len(PEERS)):
	print(names[i], PEERS[i].key)
