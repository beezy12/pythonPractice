
# really good notes for this in my Bear notebook, under Python
# connect to Google

import socket
import sys
import time

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('socket created.....')
    time.sleep(2)
except socket.error as err:
    print ('socket creation failed with an error %s' %(err))

# default port for the socket
# ALL HTTP REQUESTS BY DEFAULT USE PORT 80
port = 80

try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
    print ('there was an error resolving the host')
    sys.exit()

# connect to the server
# could also just do:
# s.connect(('www.google.com', 80))
s.connect((host_ip, port))

print ('the socket successfully connected to google on port == {}' .format(host_ip))
