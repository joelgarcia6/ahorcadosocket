from socket import socket

mi_socket = socket()
mi_socket.connect(('localhost', 8000))

mi_socket.send(str("Hiiiiii").encode('utf-8'))
res = mi_socket.recv(1024)

print(res)
mi_socket.close()