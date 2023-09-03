#UDP client code

from socket import *

#assigning a random port number of our choice
serverName = 'localhost'
serverPort = 12001

#AF_INET : IPv4 address, SOCK_DGRAM : UDP connection
clientSocket = socket(AF_INET,SOCK_DGRAM)

#input from user
message = input('Input lowercase sentence:')

clientSocket.sendto(message.encode(), (serverName,serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())

clientSocket.close()
