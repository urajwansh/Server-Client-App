import socket

host = socket.gethostname()
port = 5000

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((host,port))
    s.listen()
    conn , addr = s.accept()
    while True:
        msg = conn.recv(1024).decode() # 1024 bytes of data pockets
        if not msg:
            break
        print("From connected user "+str(msg))
        msg = input('>')
        conn.send(msg.encode())
    conn.close()
