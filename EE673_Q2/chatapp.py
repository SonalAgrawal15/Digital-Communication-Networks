# importing modules for the chat app
import socket
import time
import threading
import sys
# AF_INET = Network Address Family : IPv4
# SOCK_DGRAM = DataGram Socket : UDP

# Function for receiving
def receiver():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((ip_PC, port_PC)) # binding the IP address and port number

    while True:
        msg = s.recvfrom(1024)
        print("\n"+recvname+ ":"+ msg[0].decode())
        print(f'{name}:', end=" ")

# Function for sending
def sender():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        text = input(f'{name}:')
        text = name+":"+text
        s.sendto(text.encode(), (ip_mobile, port_mobile))

# Taking inputs from the user
print("Initializing....")

# UDP monitor mobile application data
ip_mobile = input("\nEnter the IP of receiver: ")
port_mobile = int(input("\nEnter the port of the receiver: "))

# PC data
ip_PC = input("\nEnter the IP of your system : ")
port_PC = int(input("\nEnter the port of your system: "))

# Names of the sender and receiver
name = input("Enter your name: ")
recvname = input("Enter Receiver name: ")

print("Waiting for client....")
time.sleep(1)
print("Connection established....")

# Using Multi-threading
send = threading.Thread(target=sender)
receive = threading.Thread(target=receiver)
send.start()
receive.start()