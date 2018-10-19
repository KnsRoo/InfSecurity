import random, math

def randomprime():
	prime = random.randint(32,300)
	return ((2**prime)-1, random.randint(3,10)) if 2 in [prime,2**prime%prime] else randomprime()

class Peer():
	def __init__(self,g,p):
		self.g, self.p = g, p
		self.k = random.randint(10,99)
		self.mod = (self.g**self.k)%self.p

	def getsecret(self, R, key = False):
		self.secret = (R**self.k)%self.p
		if key: self.key = self.secret
			
COUNT = 8
p,g = randomprime()
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
