import socket

## 1. construct a client socket object.
clnt_sock = socket.socket()

## 2. specify the host name
host = socket.gethostname()
## 3. specify the port
port = 1234

## 4. connect to the host on the port
clnt_sock.connect((host, port))

## 5. print the server response.
##    1024 bytes
print clnt_sock.recv(1024)
