#!/usr/bin/python>
import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind((socket.gethostname(), 1234))

mySocket.listen(5)

while True:
    print("Waiting conections")
    (clientSocket, address) = mySocket.accept()
    print("HTTP request received")
    print(clientSocket.recv(1024))
    clientSocket.send("HTTP/1.1 200 OK \r\n\r\n" +
                        "<html><body"
