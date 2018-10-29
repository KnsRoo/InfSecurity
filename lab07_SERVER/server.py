import randomtools as rt
import socket
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

def accept_incoming_connections():
    while True:
        conn, addr = server_socket.accept()
        conn.send(bytes("SYSTEM:Wonderful! Welcome to the secret messenger. Insert name and press Enter", "utf8"))
        Thread(target=on_connected, args=(conn,)).start()

def on_connected(client, packet = ''):
    name = client.recv(1024).decode("utf8")
    if name in names: name = name+str(rt.randedge(1,1000))
    clients.append(client), names.append(name)
    broadcast(bytes('SYSTEM:Online '+', '.join(names), "utf8"))
    clients[names.index(name)].send(bytes("pg:"+str(G)+":"+str(P), "utf-8"))
    while True:
        msg = client.recv(1024)
        if msg != bytes("#close", "utf8"):
            msg = msg.decode("utf8").split(':')
            if not msg[1] in names: clients[names.index(msg[0])].send(bytes('SYSTEM:'+str(msg[1])+'is Offline',"utf-8"))
            else:
                for i in range(len(msg)):
                    if i!=1: packet+=msg[i]+':'
                clients[names.index(msg[1])].send(bytes(packet, "utf-8"))
        else:
            a = clients.index(client)
            del clients[a]; del names[a]
            client.close()
            broadcast(bytes('SYSTEM:Online '+', '.join(names), "utf8"))
            break

def broadcast(msg):
    for sock in clients: sock.send(msg)

clients = names = []
P,G = rt.randomprime()
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('localhost', 8085))
server_socket.listen(10)
print("Waiting peers...")
_thread = Thread(target=accept_incoming_connections)
_thread.start()
_thread.join()
server_socket.close()
