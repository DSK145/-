  GNU nano 8.3                                                              qazxc.py                                                                        import socket #导入socket
address = input("IPv4/IPv6/4/6")
if address == "4":
   family = socket.AF_INET
   port = 80 #80端口
   server = ("github.com",port)
elif address == "6":
     family = socket.AF_INET6
     port = 22 #22端口
     server = ("github.com",port)
else:
     print ('ON')
     exit()
#套接字TCP
client_socket = socket.socket(family,socket.SOCK_STREAM)
try:
    client_socket.connect(server)
    print("oK")
    mkl = "GET / HTTP/1.1、r\nHost: {}\r\n\r\n".format(server[0])
    client_sockrt.send(message.encode()) #发送数据
    response = client_socket.recv(4096) #接收数据
    print ("ok")
    print (response.decode())
except socket.error as e:
    print (f"NO: {e}")
finally:
    print ('54088')
    client_socket.close()#关闭套接字
    def zxc():
        print("ok")
        zxc()
    