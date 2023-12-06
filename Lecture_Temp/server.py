import socket
from _thread import *

def threaded(client_socket, addr):
    print('>> Connected By : ',)
    
    while True:
        try:
            data = client_socket.recv(1024)
            
            if not data:
                print('>> Disconnected by' + addr[0], ' : ', addr[1])
                break
        
            print('>> Received from ' + addr[0], ' : ', addr[1], data.decode())
            
            for client in client_sockets:
                if client != client_socket:
                    pass
        except:
            pass 

    
    

# 서버에 접속한 클라이언트 목록
client_sockets = []

# 서버 IP 및 열어줄 포트
HOST = '127.0.0.1'
PORT = 5000

print('>> Server Start')
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(HOST,PORT)
server_socket.listen()

try:
    while True:
        print('>> Wait')

        client_socket, addr = server_socket.accept()
        client_sockets.append(client_socket)
        start_new_thread(threaded, (client_socket, addr))
        print("참가자 수 : ", len(client_sockets))
    
    
except Exception as e:
    print('에러 : ', e)
finally:
    server_socket.close()


