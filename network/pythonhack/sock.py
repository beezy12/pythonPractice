
# this program creates a simple server. to connect, open Filezilla and connect to the server using localhost on port 1249
# came from my udemy ethical hacking course
# notes in my Bear notebook
# docs here: https://docs.python.org/3.6/howto/sockets.html

import socket

# create a socket object
s = socket.socket()
print('created socket....')

# reserve a port number
port = 1249

# bind to the port
# we bind with empty string to allow the socket to connect to any IP. If I set it as localhost or 127.0.0.1, the socket would only be visible within the same machine
s.bind(('', port))
print('socket binded to %s' %(port))
# from the docs:
# serversocket.bind((socket.gethostname(), 80))


# put socket into listening mode
s.listen(5)
print('socket is listening....')

# a forever loop until we exit or an error occurs
while True:
    # establish connection with the client
    c, addr = s.accept()
    print('got connection from: ', addr)


