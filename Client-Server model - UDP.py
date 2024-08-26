#AIM: To implement a client-server communication model using UDP. 

# [ udp_server.py ]
import socket
def udp_server():
    host = socket.gethostname()
    port = 5000
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print("UDP server listening on {}:{}".format(host, port))
    while True:
        data, address = server_socket.recvfrom(1024)
        print("Received from client:", data.decode())
        server_socket.sendto("Hi from server!".encode(), address)
udp_server()

# [ udp_client.py ]
import socket
def udp_client():
    host = socket.gethostname()
    port = 5000
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.connect((host, port))
    print("UDP connection established with server")
    client_socket.sendto("Hello!".encode(), (host, port))
    data, _ = client_socket.recvfrom(1024)
    print("Received from server:", data.decode())
udp_client()
'''
_____________________________________________________
output:
[udp_server.py]
UDP server listening on ds-da-18:5000
Received from client: Hello!

[udp_client.py]
UDP connection established with server
Received from server: Hi from server!
'''
