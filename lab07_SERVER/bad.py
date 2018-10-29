from socket import socket, AF_INET, socket, SOCK_STREAM

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 8085))

while 1:
	cl = input()
	sock.send(bytes(cl, "utf8"))
