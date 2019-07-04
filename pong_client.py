import socket

host = '127.0.0.3'
port = 8000

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((host,port))
    msg = bytearray(input(),'utf8')
    s.sendall(msg)
