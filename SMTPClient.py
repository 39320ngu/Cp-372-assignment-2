#import libraries needed for communication with a secure email server
from socket import *
import ssl
import re
from email.base64mime import body_encode as encode_base64


def auth_plain(sender_email, password):
    """ Authobject to use with PLAIN authentication. Requires
    self.user and
    self.password to be set."""
    return "\0%s\0%s" % (sender_email, password)


def send_msg(message, expect_return_msg = True):
    tcpSocket.send(f"{message}\r\n".encode())
    if expect_return_msg:
        recv = recieve_msg()
        print(recv)
        return recv  

def recieve_msg():
    try:
        return tcpSocket.recv(2048).decode()
    except timeout:
        pass

"""
S: 220 hamburger.edu
C:HELO crepes.fr
S:250 Hello crepes.fr, pleased to meet you
C:MAIL FROM: <alice@crepes.fr>
S:250 alice@crepes.fr... Sender ok
C:RCPT TP: ,bob.hamburder.edu>
S:250 bob@hamburger.edu ... Recipient ok
C:DATA
S:353 Enter mail, end with"." in a line by itself
C:Do you like ketchup?
C:How about pickles?
C:.
S:250 Message accepted for delivery
C:QUIT
S:221 hamburger.edu closing connection

"""
email ='s69541071@gmail.com'
password = 'tvfy xkry bsii offd'

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server)
mailserver = 'smtp.gmail.com'

port = 587



# Make a TCP connection with mailserver and receive the server
#response
tcpSocket=socket(AF_INET, SOCK_STREAM)
tcpSocket.connect(mailserver)

tcpSocket.settimeout(10)


#check the server response and print it to the screen


recieve_msg()


# Send HELO command to the server and print server response. It should be ehlo not helo

heloCommand = 'ehlo [' + addr +']\r\n'
  
send_msg(heloCommand, True)
recieve_msg()



# Send STARTTLS command and print server response.
starttlsCommand = 'STARTTLS\r\n'

send_msg(starttlsCommand, True)
recieve_msg()


# wrap the socket you created earlier in a ssl context. Assuming you
# named you socket, clientSocket, you can use the following two lines
# to do so:



context = ssl.create_default_context()
tcpSocket = context.wrap_socket(tcpSocket, server_hostname=mailserver)

"""
Now, the client needs to authenticate to the server. The AUTH command is used for this
purpose. The AUTH command sends the clients username and password to the e-mail server.
AUTH can be combined with some other keywords such as PLAIN, LOGIN, CRAM-MD5 and
DIGEST-MD5 (e.g. AUTH LOGIN) to choose an authentication mechanism. The authentication
mechanism chooses how to login and which level of security that should be used. To
authenticate using AUTH PLAIN you do so:

Send the AUTH PLAIN command to the server.
Command = ‘AUTH PLAIN\r\n’


After the client has sent the AUTH PLAIN command to the server, the server responds with a
334 reply code. Then the username and password are sent from the client to the server. The
username and password are combined to one string and BASE64 encoded (using
encode_base64 function in python). To combine username and password you can use the
auth_plain function given above. Although the keyword PLAIN is used, the username and
password are not sent as plain text over the Internet - they are always BASE64 encoded. If you
want to read more about BASE64 encoding, look here.

"""
Command = 'AUTH PLAIN\r\n'

send_msg(Command, True)
authorization = auth_plain(email, password)

send_msg(authorization, True)


# Send DATA command and print server response.
# Send message data.
# Message ends with a single period.


send_msg("DATA", True)



message = msg + endmsg

send_msg(message, True)



# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'


send_msg(quitCommand, True)