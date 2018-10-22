import sys, socket, random

def randomprime():
	prime = random.randint(32,300)
	return ((2**prime)-1, random.randint(3,10)) if 2 in [prime,2**prime%prime] else randomprime()

def givesecret(peer, secret, final = False):
	comm = 'givf' if final else 'givs'
	msg = comm+':'+str(secret)+':'
	peer.send(msg.encode('utf-8'))
	
def getsecret(peer):
	peer.send('gets'.encode('utf-8'))
	return int(peer.recv(1024).decode('utf-8'))

def getmod(peer):
	peer.send('getm'.encode('utf-8'))
	return int(peer.recv(1024).decode('utf-8'))

def transmit():
	p,g = randomprime()
	for peer in PEERS:
		gp = 'gtgp'+':'+str(g)+':'+str(p)+':'
		peer.send(gp.encode('utf-8'))
	for i in range(len(PEERS)):
		if len(PEERS) == 2: givesecret(PEERS[(i+1)%len(PEERS)], getmod(PEERS[(i)%len(PEERS)]), final = True)
		else:
			givesecret(PEERS[(i+1)%len(PEERS)], getmod(PEERS[(i)%len(PEERS)]))
			j = i+2
			for x in range(len(PEERS)-3):
				givesecret(PEERS[j%len(PEERS)], getsecret(PEERS[(j-1)%len(PEERS)]))
				j+=1
			givesecret(PEERS[(i+len(PEERS)-1)%len(PEERS)], getsecret(PEERS[(i+len(PEERS)-2)%len(PEERS)]), final = True) 

sock = socket.socket()
sock.bind(('', 8081))
cl = int(sys.argv[1])
sock.listen(int(cl))
PEERS = []

while True:
	conn, addr = sock.accept()
	PEERS.append(conn)
	print('waiting peers', str(len(PEERS))+'/'+str(cl))
	if int(cl) == len(PEERS):
		transmit()
		while True:
			print('Repeat? y/n')
			f = input()
			if f == 'y': transmit()
			else: break
		break
sock.close()
