import socket

host = ""
port = 10789
buff_size = 128

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = (host , port)
sock.bind(server_address)

while True:
    print("Waiting for requests...")
    message, client_address = sock.recvfrom(buff_size)
    print("echo request from {} port {} ".format(client_address[0],client_address[1]))
    message.decode()
    try:
        message = int(message)
        if message % 2 == 0:
            print("짝수입니다: {}\n".format(message))
        elif message % 2 != 0:
            print("홀수입니다: {}\n".format(message))
    except ValueError:
     print("정수를 입력하세요")

sock.close()