'''
the steps are:
1. create socket
2. bind to the port
3. socket listen
4. socket connect
'''


import socket

s = socket.socket()
print('socket created.....')

port = 1666

s.bind(('', port))
print('socket binded to ', format(port))


s.listen(5)
print('socket is listening')


while True:
    c, addr = s.accept()
    print('got connection from: ', addr)


