import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
# print(SERVER)
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

#created a socket, picked a family AF_NET, picked the type SOCK_STEAM
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind the addrress to the server (it should be tuples)
server.bind(ADDR)

#wait for clients
#will run concurrently for each client
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        #this wont execute untill a msg recieved form the client (blocking code)
        #how many bytes we are going to take is inside recv() 
        #to specify that we need a header (always so it should be 64 bytes)
        msg_length = conn.recv(HEADER).decode(FORMAT)
        #convert it to int
        msg_length= int(msg_length)
        #put that here as how many byte recieved
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False
        print(f"[{addr}] {msg}")

    conn.close()


#start the socket server
#allow connections and handling them
def start():
    server.listen()
    while True:
        #when new con occured addrress will store in the addr
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        #substract 1 because always a thread is running the starting thread
        #number of threads equal number of connections
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()