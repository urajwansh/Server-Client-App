import socket

host = socket.gethostname();
port = 5000

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((host,port))
    c_msg = input(' > ')
    while c_msg.lower().strip() != 'bye':
        s.send(c_msg.encode())
        s_msg = s.recv(1024).decode()

        print('Received form server: '+s_msg)
        c_msg = input(' > ')
    s.close()
