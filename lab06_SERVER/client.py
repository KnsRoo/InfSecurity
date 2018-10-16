import socket, random

class Peer():
	def __init__(self,g,p):
		self.g, self.p = g, p
		self.k = random.randint(10,99)
		self.mod = (self.g**self.k)%self.p

	def getsecret(self, R, key = False):
		self.secret = (R**self.k)%p
		if key: self.key = self.secret


sock = socket.socket()
sock.connect(('localhost', 8081))
client = None

while True:
	comm = sock.recv(1024)
	comm = comm.decode('utf-8')
	if comm == 'gp':
		gp = sock.recv(1024)
		gp = gp.decode('utf-8')
		gp = gp.split(':')
		g = int(gp[0])
		p = int(gp[1])
		client = Peer(g,p)
	elif comm == 'getm': 
		sock.send(str(client.mod).encode('utf-8'))
	elif comm == 'gets': 
		sock.send(str(client.secret).encode('utf-8'))
	elif comm == 'gives':
		secret = sock.recv(1024)
		client.getsecret(int(secret.decode('utf-8')))
	elif comm == 'givesf':
		key = sock.recv(1024) 
		client.getsecret(int(key.decode('utf-8')), key = True)
		print('My key ', client.key)
	else:
		print('Command',comm,'is invalid')
	comm = ''

sock.close()
