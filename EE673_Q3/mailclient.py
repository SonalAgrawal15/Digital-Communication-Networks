from socket import *
import base64 #encoding/decoding
import getpass  #used to deal with confidential data-password in our case
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

#iitk mail server and port number
mailServer = 'mmtp.iitk.ac.in'
mailPort = 25

print("Creating the socket..")

#creating a TCP connection
clientSocket = socket(AF_INET, SOCK_STREAM)

print("Connecting the socket..")

clientSocket.connect((mailServer,mailPort))

print("Connection established")
recv = clientSocket.recv(1024)

print("This is the recv: %s" % recv.decode())

#error messages to trace error point
if recv[:3] != b'220':
    print ('220 reply not received from server.')

#The HELO command initiates the SMTP session conversation
helo = 'HELO iitk.ac.in\r\n'
clientSocket.send(helo.encode())

#error messages to trace error point
recv1 = clientSocket.recv(1024)
print("This is the recv1: %s" % recv1.decode())
if recv1[:3] != b'250':
    print('250 reply not received from server.')

Username = input('Enter your email address: ')
Password = input('Enter Password: ')
# Password = getpass.getpass(prompt="Insert Password: ")
#encoding username and password into base64 for security
UP = base64.b64encode(("\000"+Username+"\000"+Password).encode()).decode()

#logging in using the username and password using the AUTH PLAIN command of STMP
print(UP)
UP=UP.strip("\n")
login = 'AUTH PLAIN '+ UP + '\r\n'
print(login)
clientSocket.send(login.encode())
recv_from_TLS = clientSocket.recv(1024)
print(recv_from_TLS)

#sending encoded sender data using the MAIL FROM Command
mailfrom = 'MAIL FROM: <'+ Username+'>\r\n'
print(mailfrom)
clientSocket.send(mailfrom.encode())
recv2 = clientSocket.recv(1024)
#error detection
print("This is the recv2: %s" % recv2)
if recv2[:3] != b'250':
    print('rcpt2 to 250 reply not received from server.')

#taking user input for receiver details - receivers list is for taking multiple receiver email ids in 'to' section, CClist for CC receiver and BCC list for BCC receivers of the email
receivers = [x for x in input("Enter receiver email addresses seperated by commas: ").split(",")]
tolist = ','.join(receivers)
CC = [c for c in input("CC to: ").split(",")]
CClist = ','.join(CC)
BCC = [m for m in input("BCC to: ").split(",")]
BCClist = ','.join(CC)

#dislaying the 'to' data and sending using RCPT TO command (loop used for multiple receivers)
print('RCPT TO: <', end=" ")
for y in receivers:
    toCommand = 'RCPT TO: <'+ y +'>\r\n'
    print(*receivers, sep=", ", end=" ")
    clientSocket.send(toCommand.encode())
print('>')

#displaying the CC data using RCPT TO command (loop used for multiple receivers)
print('CC TO: <', end=" ")
for z in CC:
    toCommand = 'RCPT TO: <'+ z +'>\r\n'
    print(*CC, sep=", ", end=" ")
    clientSocket.send(toCommand.encode())
print('>')

#displaying the BCC data using RCPT TO command (loop used for multiple receivers)
print('BCC TO: <', end=" ")
for w in BCC:
    toCommand = 'RCPT TO: <'+ w +'>\r\n'
    print(*BCC, sep=", ", end=" ")
    clientSocket.send(toCommand.encode())
print('>')

#error detection
recv3 = clientSocket.recv(1024)
print("This is the recv3: %s" % recv3)
if recv3[:3] != b'250':
    print('rcpt3 to 250 reply not received from server.')

# Create a MIME Multipart message
msg = MIMEMultipart()
msg['From'] = Username
msg['To'] = tolist
msg['Cc'] = CClist
msg['Subject'] = input("Subject: ")

# Attach the message body
message_text = input("Body: ")
msg.attach(MIMEText(message_text, 'plain'))

# Attachments handling
attachment_paths = input("Enter paths to attachments separated by commas: ").split(',')
for attachment_path in attachment_paths:
    with open(attachment_path, 'rb') as attachment_file:
        attachment = MIMEApplication(attachment_file.read())
        attachment.add_header('Content-Disposition', 'attachment', filename=attachment_path.split("\\")[-1])
        msg.attach(attachment)

endmsg = "\r\n.\r\n"
# Send the message as a string
clientSocket.send('DATA\r\n'.encode())
clientSocket.send(msg.as_string().encode())
clientSocket.send(('\r\n' + endmsg).encode())
clientSocket.close()
print("Connection closed")