import socket, random, _thread, time

def randomprime():
	prime = random.randint(32,300)
	return ((2**prime)-1, random.randint(3,10)) if 2 in [prime,2**prime%prime] else randomprime()

def givesecret(peer, secret, final = False):
	if final: peer.send('givesf'.encode('utf-8'))
	else: peer.send('gives'.encode('utf-8'))
	time.sleep(1)   # Кастыль
	peer.send(str(secret).encode('utf-8'))
	
def getsecret(peer):
	peer.send('gets'.encode('utf-8'))
	secret = peer.recv(1024)
	secret = int(secret.decode('utf-8'))
	return secret

def getmod(peer):
	peer.send('getm'.encode('utf-8'))
	mod = peer.recv(1024)
	mod = int(mod.decode('utf-8'))
	return mod

def start(conn, addr):
	global g
	global p
	for peer in PEERS:
		gp = str(g)+':'+str(p)
		peer.send('gp'.encode('utf-8'))
		peer.send(gp.encode('utf-8'))
	for i in range(len(PEERS)):
		if len(PEERS) == 2:
			a = getmod(PEERS[(i)%len(PEERS)])
			givesecret(PEERS[(i+1)%len(PEERS)], a, final = True)
		else:
			a = getmod(PEERS[(i)%len(PEERS)])
			print(a)
			givesecret(PEERS[(i+1)%len(PEERS)], a)
			j = i+2
			for x in range(len(PEERS)-3):
				a = getsecret(PEERS[(j-1)%len(PEERS)])
				print(a)
				givesecret(PEERS[j%len(PEERS)], a)
				j+=1
			a = getsecret(PEERS[(i+len(PEERS)-2)%len(PEERS)])
			print(a)
			givesecret(PEERS[(i+len(PEERS)-1)%len(PEERS)], a, final = True)

sock = socket.socket()
sock.bind(('', 8081))
print('Insert count of clients')
cl = input()
sock.listen(int(cl))
p,g = randomprime()
PEERS = []

while True:
	conn, addr = sock.accept()
	PEERS.append(conn)
	print('waiting peers', str(len(PEERS))+'/'+str(cl))
	if int(cl) == len(PEERS):
		_thread.start_new_thread(start,(conn,addr))
conn.close()