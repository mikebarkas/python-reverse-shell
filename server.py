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
        print('Error creating socket: ' + str(e))


def socket_bind():
    try:
        global host
        global port
        global s

        print('Binding socket and port: ' + str(port))
        s.bind((host, port))
        s.listen(3)

    except socket.error as e:
        print('Binding socket error: ' + str(e))
        print('Retrying..')
        socket_bind()


def socket_accept():
    conn, address = s.accept()
    print('Connection created: ' + address[0] + ' : ' + str(address[1]))
    send_commands(conn)
    conn.close()


def send_commands(conn):
    while True:
        cmd = input()

        if len(str.encode(cmd)) > 0:
            if cmd == 'quit':
                conn.close()
                s.close()
                sys.exit()
            else:
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(1024), 'utf-8')
                print(client_response, end='')


def main():
    socket_create()
    socket_bind()
    socket_accept()


main()