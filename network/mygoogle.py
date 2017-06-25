
import socket
import sys
import time


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('socket created....')
    time.sleep(1)
except socket.error as err:
    print('socket creation failed with ', format(err))

port = 80

try:
    host_ip = socket.gethostbyname('www.rotogrinders.com')
except socket.gaierror:
    print('there was an error resolving the host')
    sys.exit()

s.connect((host_ip, port))

print('socket connected to port ', format(host_ip))
