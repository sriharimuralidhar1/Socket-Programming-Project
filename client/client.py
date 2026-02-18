import time
import socket
#initializing host, port and filename
host = '10.0.75.1'
port = 65500
fileName = "send.txt" # existing file to be sent to the server
for i in range(1,101):
    print('Client is connecting to the server: ', host,'\n')

    #connecting to the server
    client_s = socket.socket()
    # equivalent to socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # address family is AF_INET (Ipv4, by default)
    # socket type is SOCK_STREAM (TCP, by default)

    client_s.connect((host, port))
    # establish a connection to the server and initiate the three-way handshake

    print('I am sending file', fileName," for the ",i," time")
    #open file to read
    file_to_send = open(fileName, 'rb')
    # 'b' means the file will be handled in binary mode

    #read the first 1024 bits from the file
    data = file_to_send.read(1024)

    while data:
        client_s.send(data)
        # Send data to server thru the socket
        # The socket must be connected to a remote socket

        #read the next 1024 bits from the file
        data = file_to_send.read(1024)

    print('I finished sending the file', fileName," for the ",i," time")

    file_to_send.close()
    client_s.close()
    time.sleep(1)

print('All tasks of client is done')
