#Student Daniel Nguyen 201001070


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
    tcpSocket.send(f"{message}".encode())
    if expect_return_msg:
        recv = recieve_msg()
        print(recv)
        return recv  

def recieve_msg():
    try:
        return tcpSocket.recv(2048).decode()
    except timeout:
        pass




email ='s69541071@gmail.com'
password = 'tvfy xkry bsii offd'

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server)

port = 587
mailserver = ('smtp.gmail.com', port)





# Make a TCP connection with mailserver and receive the server
#response
tcpSocket=socket(AF_INET, SOCK_STREAM)
tcpSocket.connect(mailserver)

tcpSocket.settimeout(10)


#check the server response and print it to the screen

print(" Connect to mailserver")
recieve_msg()


# Send HELO command to the server and print server response. It should be ehlo not helo

heloCommand = 'ehlo [' + "test" +']\r\n'
send_msg(heloCommand, True)




# Send STARTTLS command and print server response.
starttlsCommand = 'STARTTLS\r\n'
send_msg(starttlsCommand, True)



# wrap the socket you created earlier in a ssl context. Assuming you
# named you socket, clientSocket, you can use the following two lines
# to do so:



context = ssl.create_default_context()
tcpSocket = context.wrap_socket(tcpSocket, server_hostname=mailserver[0])

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

byte_user = encode_base64(auth_plain(email, password).encode())

authorization = 'AUTH PLAIN ' + byte_user




print("Sending Authorization")
send_msg(authorization, True)


# Send DATA command and print server response.
# Send message data.
# Message ends with a single period.

message = msg + endmsg


send_msg(f"MAIL FROM:<{email}>\r\n")
send_msg(f"RCPT TO:<{email}>\r\n")
send_msg(f"DATA\r\n")
send_msg(f"SUBJECT: Test email sent\r\n", expect_return_msg=False)
send_msg(message, False)






# Send QUIT command and get server response.
quitCommand = 'QUIT'


send_msg(quitCommand, True)