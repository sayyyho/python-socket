import socket

host = '127.0.0.1'
port = 9123

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

while True:
    msg = input("input msg : ")
    client_socket.sendall(msg.encode("utf-8"))
    if msg == "quit":
        break
    receive_data = client_socket.recv(1024)
    print(f"receive : {receive_data.decode('utf-8')}")

client_socket.close()
print("접속을 종료합니다.")

# https://sungmin-joo.tistory.com/56