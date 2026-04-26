import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)

print('Connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    while True:
        message = input("Enter your problem (or 'exit'): ")

        if message.lower() == 'exit':
            break

        sock.sendall(message.encode('utf-8'))

        data = sock.recv(1600)
        print()
        print("Server:", data.decode('utf-8'))
        print()

finally:
    print("Closing socket")
    sock.close()