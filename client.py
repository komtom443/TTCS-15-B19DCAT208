import socket

clientMessage = "Hello, I am B19DCAT208 client"
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",55555))

client.send(clientMessage.encode("ascii"))
while True:
    print(client.recv(1024).decode('ascii'))