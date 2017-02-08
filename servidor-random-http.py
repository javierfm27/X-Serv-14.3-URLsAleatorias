#!/usr/bin/python
import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind((socket.gethostname(), 1236))

mySocket.listen(5)

while True:
    print("Waiting conections")
    (clientSocket, address) = mySocket.accept()
    print("HTTP request received")
    print(clientSocket.recv(1024))
    clientSocket.send("HTTP/1.1 200 OK \r\n\r\n" +
                        "<html><body><h2><B>DE ECHENIQUE </B></h2>" +
                        "<img> src='http://img01.heraldo.es/uploads/imagenes/bajacalidad/2014/10/27/_echenique_7c91153f.jpg'");
    clientSocket.close();
