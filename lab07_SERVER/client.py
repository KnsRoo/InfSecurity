import socket, select, sys, os
import randomtools as rt
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

class Peer():
	def __init__(self, g, p):
		self.g, self.p = int(g), int(p)

	def hash(self, phrase):
		return sum([ord(i) for i in phrase]) % (self.p-1)

	def create_sign(self, phrase):
		x = rt.randedge(1,self.p)
		k, inv = rt.randomk(self.p)
		m = self.hash(phrase)
		y, r = pow(self.g , x, self.p), pow(self.g, k, self.p)
		s = ((m-x*r)*inv) % (self.p-1)
		return [y, r, s]

	def check_sign(self, sign):
		if (0 < int(sign[3]) < self.p) and (0 < int(sign[4]) < self.p-1):
			m = self.hash(sign[1])
			return True if (pow(int(sign[2]),int(sign[3]),self.p)*pow(int(sign[3]),int(sign[4]),self.p)) % self.p == pow(self.g, m , self.p) else False
		else: return False

def print_(string):
	print(string)
	history.append(string)

def receive():
    global Client
    while True:
        try:
            msg = sock.recv(1024).decode("utf8")
            msg = msg.split(':')
            if msg[0] == 'pg': Client = Peer(msg[1],msg[2])
            elif msg[0] == 'SYSTEM': print_(msg[1])
            else:
            	if Client != None:
                    if (Client.check_sign(msg)): print_(msg[0]+':'+msg[1])
                    else: print_('Sign invalid')
        except OSError: break

def send(msg): 
	if msg != "#close":
		tmp = msg.split(':')
		if Client != None:
			sign = Client.create_sign(tmp[1])
			msg = str(Name)+':'+msg+':'+str(sign[0])+':'+str(sign[1])+':'+str(sign[2])
		sock.send(bytes(msg, "utf8"))
	else: 
		sock.send(bytes("#close", "utf-8"))
		sock.close()
		exit(0)

history, Client = [], None
Name, ex = None, False
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 8085))
_thread = Thread(target=receive)
_thread.start()
while 1:
	cl = input()
	os.system('cls');
	for item in history: print(item)
	print_('You -> '+cl)
	if not ex: 
		Name = cl
		ex = True 
	send(cl)