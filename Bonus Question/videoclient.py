from socket import *

#assigning server name and port number : port number can be nay number - should be same in videoserver file
serverName = 'localhost'
serverPort = 12006

#creating the TCP connection and connecting to server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

#User inputs
print('*** This is video streaming code ***')
sentence = input('Do you want to stream your live video? y/n: ')

clientSocket.send(sentence.encode())

modifiedSentence = clientSocket.recv(1024)

print('From Server: ', modifiedSentence.decode())
clientSocket.close()