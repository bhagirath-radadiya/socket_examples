# client.py

import socket
import threading

HOST = '127.0.0.1'
PORT = 9000

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
client_socket.connect((HOST, PORT))
print("Connected to server!")


def in_msg():
    while True:
        data = client_socket.recv(1024)
        if data:
            message = data.decode()
            print(f"Received message: {message}")

def out_msg():
    while True:
        message = input()
        client_socket.send(message.encode())

t1 = threading.Thread(target=in_msg)    
t2 = threading.Thread(target=out_msg)

t1.start()
t2.start()



# server.py

import socket
import threading

HOST = '127.0.0.1'
PORT = 9000

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a specific address and port
server_socket.bind((HOST, PORT))

# listen for incoming connections
server_socket.listen(5)

# accept a client connection
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address} has been established!")


def in_msg():
    while True:
        data = client_socket.recv(1024)
        if data:
            message = data.decode()
            print(f"Received message: {message}")

def out_msg():
    while True:
        message = input()
        client_socket.send(message.encode())

t1 = threading.Thread(target=in_msg)
t2 = threading.Thread(target=out_msg)

t1.start()
t2.start()
