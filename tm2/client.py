
import socket
import hashlib
from threading import Event

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",55555))
clientMessage = "Day la tin nhan tu B19DCAT208 client"
key = "208"



client.send(clientMessage.encode("ascii"))
Event().wait(5)
client.send(hashlib.md5(str.encode(clientMessage + key)).digest())
