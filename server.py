import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
# print(SERVER)
ADDR = (SERVER, PORT)

#created a socket, picked a family AF_NET, picked the type SOCK_STEAM
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind the addrress to the server (it should be tuples)
server.bind(ADDR)

#wait for clients
def handle_client(conn, addr):
    pass

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