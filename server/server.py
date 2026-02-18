import socket
import filecmp
file2 = 'sent.txt'       #Sample file to compare
#initializing host and port
HOST = '10.0.75.1'
PORT = 65500
#starting the server
error_ct = 0
for i in range(1,101):
    # Here we made a socket instance and passed it two parameters
    # The first parameter is the address family AF_INET, it refers to IPv4
    # The second one is the socket type SOCK_STREAM, which means the socket type is TCP
    server_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_s.bind((HOST, PORT))
    # Bind the socket to an address (HOST, PORT)

    server_s.listen(5)
    # s.listen(backlog) Listen for connections made to the socket
    # The backlog argument specifies the maximum number of queued connections
    # and should be at least 1; the maximum value is usually 5
    print('Server is listening for client requests \n')

    conn, addr = server_s.accept()
    # Accept a connection. The return value is a pair (conn, address)
    # conn is a new socket object usable to send and receive data on the connection
    # address is the (HOST, PORT) bound to the socket on the other end of the connection

    file = 'receive'; # to store all received data

    print('I am receiving the file and saving it into a file ', file+'_'+str(i)+'.txt'," for the ",i," time")

    #opening the file to write
    f = open(file+'_'+str(i)+'.txt', 'wb')
    data = conn.recv(1024)
    # Receive data from the socket. The return value is a string representing the data received
    # The maximum amount of data to be received at once is specified by buf_size
    # b means the file will write in binary mode
    while (data):
        f.write(data)
        data = conn.recv(1024)
    f.close()  # Close the file
    print('I finished receiving and saving the file ', file+'_'+str(i)+'.txt')
    comp = filecmp.cmp(file+'_'+str(i)+'.txt', file2,shallow = False)

    # Print the result of comparison
    print('True or False: Does the file match up with the Orginal file? ',comp)
    if not (comp):
        error_ct += 1

    conn.close() #close the socket
    server_s.close() #close the server

print('All tasks of server is done')
print ("The number of incorrect transfers over" ,i, "transfers  is: ", error_ct)
