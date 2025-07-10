import socket

host = 'localhost'
port = int(input("端口号开放/无占用: "))
TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCP.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
    TCP.bind((host, port))
    TCP.listen(10)
    print ("--------------------------------------------")
    print("监听端端口号/目前用TCP连接无加密: ", port)
    if TCP:
        conn, addr = TCP.accept()
        print("连接地址是IPV4: ", addr)
        while True:
            try:
                response = conn.recv(6000).decode('utf-8')
                print("接收数据小心SQL: ", response)
                response_message = input("回复:")
                encoded_response = response_message.encode('utf-8')
                conn.send(encoded_response)
            except socket.error as e:
                print(f"接收或发送数据时出错中止: {e}")
                break
        conn.close()
    TCP.close()    