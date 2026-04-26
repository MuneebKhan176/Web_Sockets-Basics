import socket
from brain import get_response

# ---------- Server ----------
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
sock.bind(server_address)

print('Starting up on %s port %s' % server_address)

sock.listen(1)

while True:
    print("Waiting for a connection")
    connection, client_address = sock.accept()

    try:
        print("Connection Established:", client_address)

        while True:
            data = connection.recv(1600)

            if data:
                message = data.decode('utf-8')
                print("User Problem:", message)

                # Smart response instead of echo
                reply = get_response(message)

                connection.sendall(reply.encode('utf-8'))

            else:
                print("No more data from", client_address)
                break

    finally:
        connection.close()