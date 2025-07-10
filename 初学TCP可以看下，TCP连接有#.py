# Tcp数据传输
import socket  # 库socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#用Tcp
server_address = ('localhost', 80)#本地80端口/localhost表127.0.0.1
server_socket.bind(server_address)
server_socket.listen(15)#监听15指15人
print ('等待TCP成功~')#print等带TCP成功
while 1:
    client_socket, client_socket = servet_socket.accept()
    print (f"连接来自{client_socket}")#{client_socket}指客户端/IP
    try: #try判断/异常处理代码块
        data =client_socket.recv(1024)#接收1024字节
        if data: #if判断
            received_data = data.decode('utf-8')#用utf-8解码
            print (f'数据；{received_data}')#{received_data}接收数据
            response = 'OK'
            client_socket.send(response.encode('utf2-8'))#utf-8编码
    finally: 
         client_socket.close()#关闭套接字