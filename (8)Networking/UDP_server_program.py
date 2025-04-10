#UDP Server program Example
import socket

#Create a UDP Socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#Bind the socket to the port

server_address = ('localhost',12345)
print('Starting up on {} port {} '.format(*server_address))
sock.bind(server_address)


while  True:
    print("\n Waiting to reeive message ")
    data , address = sock.recvfrom(4096)

    print("Received {} bytes from {}".format(len(data),address))
    print(data.encode())

    if data:
        sent = sock.sendto(data , address)
        print('Sent {} bytes back to {}'.format(sent,address))
