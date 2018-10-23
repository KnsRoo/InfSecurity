import socket, random

class Peer():
	def __init__(self,g,p):
		self.g, self.p = g, p
		self.k = random.randint(10*10,10**100)
		self.mod = pow(self.g,self.k,self.p)

	def getsecret(self, R, key = False):
		self.secret = pow(R,self.k,self.p)
		if key: self.key = self.secret

def reply(comm):
	global client
	switch = comm.pop(0)
	if switch != '':
		if switch == 'gtgp':
			g = int(comm.pop(0))
			p = int(comm.pop(0))
			client = Peer(g,p)
		elif switch == 'getm': sock.send(str(client.mod).encode('utf-8'))
		elif switch == 'gets': sock.send(str(client.secret).encode('utf-8'))
		elif switch == 'givs' or switch == 'givf':
			key = True if switch == 'givf' else False
			client.getsecret(int(comm.pop(0)), key)
			if switch == 'givf': print('My key ', client.key) 
		else: print('Command',comm,'is invalid')
		if comm: reply(comm)

sock = socket.socket()
sock.connect(('localhost', 8081))
client = None

while True:
	comm = sock.recv(1024)
	comm = comm.decode('utf-8').split(':')
	reply(comm)

sock.close()
