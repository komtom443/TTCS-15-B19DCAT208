import socket
import hashlib

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1',55555))
server.listen()
key = "208"


while True:
    client,address = server.accept()
    clientMessage = client.recv(1024).decode('ascii')
    hashCode = client.recv(1024)
    if(hashlib.md5(str.encode(clientMessage + key)).digest()== hashCode):
        print(clientMessage)
    else:
        print("The received message has lost its integrity")
    