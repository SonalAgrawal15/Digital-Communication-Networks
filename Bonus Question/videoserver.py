from socket import *

#setting serverport number, can be nay number - should be same in videoclient file
serverPort = 12006

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))

serverSocket.listen(1)
print('The server is ready to receive')

#function to call cv2code file if client response is 'y', exit otherwise.
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    if sentence == 'y':
        sendmsg = "Streaming video now.. press 'q' to exit"
        connectionSocket.send(sendmsg.encode())
        import cv2code
    # capitalizedSentence = sentence.upper()
    else:
        sendmsg = 'Exiting live stream'
        connectionSocket.send(sendmsg.encode())
    connectionSocket.close()