#AIM: To implement a client-server communication model using TCP. 

# [ client.py ]
import socket
def client():
    host = socket.gethostname()
    client_socket = socket.socket()
    client_socket.connect((host, port:=5000))
    print("Connection established with server")
    client_socket.send("Hello!".encode())  #Send data to server
    data = client_socket.recv(1024).decode()  #Receive data from server
    print("Received from server:", data)
    client_socket.close()  
client()

# [ server.py ]
import socket
def server():
    host = socket.gethostname()
    server_socket = socket.socket()
    server_socket.bind((host, port:=5000))
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Server listening on {}:{}".format(host, port))
    print("Connection established with ", address)
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("Received from client:", data)
        conn.send("Hi from server!".encode())
    conn.close()
server()
'''
_____________________________________________________
output:

[server.py]
Server listening on ds-da-18:5000
Connection established with  ('127.0.0.1', 57532)
Received from client: Hello!

[client.py]
Connection established with server
Received from server: Hi from server!
'''
