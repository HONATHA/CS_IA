import socket

host = '127.0.0.1'
port = 8080

# building the client

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as my_socket:
    my_socket.connect((host,port))
    my_socket.sendall(b'BRUHHHHHH')
# creates a socket using the AF_INET and SOCK_STREAM
# my_socket = socket.socket(socket.AF_INET.socket.SOCK_STREAM)
# my_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
# my_socket.bind((host.port))

# AF_INET: This means that we plan to use IP addresses that use 4 bytes, which are called IPv4. There is another version call AF_INET6 for the new set of IP address. 

# my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# my_socket.bind((host, port))

# maintain_connection = True
# while maintain_connection:
#     my_socket.listen()
#     connection, address = my_socket.accept()

#     while True:
#         data = connection.recv(1024)
#         data = data.decode("utf-8")
#         if not data:
#             break
#         print(str(address[0]) + ":", data)
#     connection.close()
# my_socket.close()

