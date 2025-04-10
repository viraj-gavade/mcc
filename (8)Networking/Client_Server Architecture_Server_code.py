#server side script
import socket
import time

#create a socket object
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#get local machine name
host = socket.gethostname()

port = 9999

serversocket.bind((host,port))

#queue upto 5 request
serversocket.listen(5)

while True:
    #establish connection
    clientsocket,addr = serversocket.accept()
    print("Connected to %s"%str(addr))
    currenttime=time.ctime(time.time())+"\r\n"
    clientsocket.send(currenttime.encode("ascii"))
    clientsocket.close()
