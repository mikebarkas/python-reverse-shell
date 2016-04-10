import socket
import sys


def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()

    except socket.error as e:
        print 'Error creating socket: ' + str(e)

def socket_bind():
    try:
        global host
        global port
        global s

        print'Binding socket and port: ' + str(port)
        s.bind((host, port))
        s.listen(3)

    except socket.error as e:
        print 'Binding socket error: ' + str(e)
        print 'Retrying..'
        socket_bind()
