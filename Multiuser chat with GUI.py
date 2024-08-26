# AIM: To implement multiuser chat service with TCP having a GUI.

# [ multichat_server.py ]
import socket, threading
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 55555))
server.listen()
clients = {}
def broadcast(message):
    for client in clients.values():
        client.send(message)
def handle(client, nickname):
    while True:
        try:
            message = client.recv(1024)
            if not message: break
            broadcast(f"{nickname}: {message.decode()}".encode())
        except: break
    client.close()
    del clients[nickname]
    broadcast(f'{nickname} left the chat!'.encode())
def receive():
    while True:
        client, _ = server.accept()
        client.send('NICK'.encode())
        nickname = client.recv(1024).decode()
        if nickname in clients:
            client.send('NICK_TAKEN'.encode())
            client.close()
        else:
            clients[nickname] = client
            broadcast(f"{nickname} joined the chat!".encode())
            threading.Thread(target=handle, args=(client, nickname)).start()
receive()

# [ multichat_client.py ]
import socket, threading, tkinter as tk
from tkinter import simpledialog, scrolledtext
class ChatClient:
    def __init__(self, host, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        self.nickname = simpledialog.askstring("Nickname", "Enter your nickname")      
        self.root = tk.Tk()
        self.root.title(f"Chat - {self.nickname}")
        self.text_area = scrolledtext.ScrolledText(self.root, state='disabled')
        self.text_area.pack(expand=True, fill='both')
        self.input_area = tk.Text(self.root, height=3)
        self.input_area.pack(fill='x')
        tk.Button(self.root, text="Send", command=self.write).pack()     
        threading.Thread(target=self.receive).start()
        self.root.protocol("WM_DELETE_WINDOW", self.stop)
        self.root.mainloop()
    def write(self):
        message = self.input_area.get('1.0', 'end').strip()
        if message: 
            self.client.send(message.encode())
            self.input_area.delete('1.0', 'end')
    def display_message(self, message):
        self.text_area.config(state='normal')
        self.text_area.insert('end', message + '\n')
        self.text_area.yview('end')
        self.text_area.config(state='disabled')
    def stop(self):
        self.client.close()
        self.root.destroy()
    def receive(self):
        while True:
            try:
                message = self.client.recv(1024).decode()
                if message == 'NICK':
                    self.client.send(self.nickname.encode())
                elif message == 'NICK_TAKEN':
                    print("Nickname already taken.")
                    self.stop()
                else:
                    self.display_message(message)
            except: 
                print("Connection lost!")
                self.stop()
ChatClient('127.0.0.1', 55555)
