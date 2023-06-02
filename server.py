import socket

host = "127.0.0.1"
port = 9123

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((host, port))

server_socket.listen()

client_socket, addr = server_socket.accept()

print("클라이언트의 정보 : ", addr)

while True:
    msg = client_socket.recv(1024).decode("utf-8")
    if msg == "quit": 
        break
    print(f"recieve : {msg}")
    client_socket.sendall(msg.encode())

print("접속을 종료합니다.")
client_socket.close()
server_socket.close()