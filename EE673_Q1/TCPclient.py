from socket import *

serverName = 'localhost'
serverPort = 12000

#AF_INET : IPv4 address, SOCK_STREAM : TCP connection
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

#input from user
sentence = input('Input lowercase sentence:')

clientSocket.send(sentence.encode())

modifiedSentence = clientSocket.recv(1024)

print('From Server: ', modifiedSentence.decode())
clientSocket.close()