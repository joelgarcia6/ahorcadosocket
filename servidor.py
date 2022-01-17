from socket import socket

mi_socket = socket()
mi_socket.bind(('localhost', 8000))
mi_socket.listen(5)

while True:
    con, addr = mi_socket.accept()
    print("Nueva con {}".format(addr))
    con.send(str("Hello there!").encode('utf-8'))
    con.close()