#!/usr/bin/python
import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind((socket.gethostname(), 1231))

mySocket.listen(5)

while True:
    print("Waiting conections")
    (clientSocket, address) = mySocket.accept()
    print("HTTP request received")
    print(clientSocket.recv(1024))
    clientSocket.send('HTTP/1.1 200 OK\r\n\r\n' +
                      '<html> <body> <section> Hola. <a href='+
                      str(random.randint(0,1000)) +
                      '> Dame otra </a>' +
                      '</section> </body> </html>')
    clientSocket.close();
