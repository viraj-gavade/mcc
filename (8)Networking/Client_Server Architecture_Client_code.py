import socket
#create a socket object
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#get local machine name
host = socket.gethostname()

port = 9999

#connection to hostname on the port
s.connect((host,port))

#recive no more than 1024 bytes
tm=s.recv(1024)



s.close()
print("The time is :%s"% tm.decode('ascii'))
