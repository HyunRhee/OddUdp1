import socket

host = '127.0.0.1'
port = 10789
buff_size = 128

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = (host, port)

message = input("Enter message :")
message = bytes(message, encoding='utf-8')
try:
    byte_sent = sock.sendto(message, server_address)
except Exception as e:
    print("Exception : {}".format(str(e)))

sock.close()