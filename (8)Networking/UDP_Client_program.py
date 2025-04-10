#UDP Client side
import socket

#create a UDP socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server_address = ('localhost',12345)

try:
    #send data
    message = b'This is the message . It will be echoed.'
    print('Sending {!r}'.format(message))
    sent = sock.sendto(message,server_address)

    #Receivie response
    print('Waiting to recieve')
    data,server = sock.recvfrom(4096)
    print('Received {!r}'.format(data))


finally:
    print('Closing socket')
    sock.close()
