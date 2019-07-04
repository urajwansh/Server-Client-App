import socket

host = '127.0.0.3'
port = 8000

with  socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((host,port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('connected by ',addr)
        while conn.recv(1024):
            print('Pong from server')
