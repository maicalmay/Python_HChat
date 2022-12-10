import socket
print("client")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("输入要连接的服务器ip:")
ip = input()
sock.connect((ip, 8000))
 
while True:
    recv = sock.recv(1024).decode()
    print(recv)
    if recv == "break":
        break
    sendData = input(">>>").encode()
    if sendData == "break":
        break
    sock.send(sendData)
 
sock.close()
print('ConnectionResetError: [WinError 10054] 远程主机强迫关闭了一个现有的连接。')
input('已退出,按任意键继续...')