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


msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server)
mailserver = 'smtp.gmail.com'


# Make a TCP connection with mailserver and receive the server
#response
tcpSocket=socket(AF_INET, SOCK_STREAM)
#check the server response and print it to the screen



# Send HELO command to the server and print server response. It should be ehlo not helo

heloCommand = 'ehlo [' + addr +']\r\n'


# Send STARTTLS command and print server response.
starttlsCommand = 'STARTTLS\r\n'
# wrap the socket you created earlier in a ssl context. Assuming you
# named you socket, clientSocket, you can use the following two lines
# to do so:



context = ssl.create_default_context()
clientSocket = context.wrap_socket(clientSocket, server_hostname=mailserver)


# Send DATA command and print server response.
# Send message data.
# Message ends with a single period.
message = msg + endmsg
# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'



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