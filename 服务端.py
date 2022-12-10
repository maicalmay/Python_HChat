import socket
print("server")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("定义服务器ip:")
ip = input()
sock.bind((ip, 8000))
print('服务器ip:',ip)
sock.listen(10)
while True:
    con, add = sock.accept()
    print("%s:%s  is connect"%add)
    while True:
        sendData = input(">>>").encode()
        con.send(sendData)
        if sendData == "break".encode():
            break
        recv = con.recv(1024)  
        print(recv.decode())
        if recv == "break":
            break
sock.close()
print('ConnectionResetError: [WinError 10054] 远程主机强迫关闭了一个现有的连接。')
input('已退出,按任意键继续...')