#to run this in another pc, download client code code and run it in it. If both are in the same network this will work
import socket
#to send objects rather than strings
import pickle

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

#to send msgs
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    #need to find the length of this message
    #'b' means byte space
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("HEllow World")
#can hold untill the keypress
input()
send("HEllow guys")
input()
send("HEllow john")

send(DISCONNECT_MESSAGE)