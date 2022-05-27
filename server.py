import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1',55555))
server.listen()


while True:
    client,address = server.accept()
    print(client.recv(1024).decode('ascii'))
    client.send("Hello, I am B19DCAT208 server".encode('ascii'))


