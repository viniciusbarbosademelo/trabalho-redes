import socket
import threading

bind_ip = '127.0.0.1'
bind_port = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)

print('Escutando IP e Porta: {}:{}'.format(bind_ip, bind_port))

def handle_client_connection(client_socket):
    request = client_socket.recv(1024)
    print('Recebido {}'.format(request))
    client_socket.send('Recebido'.encode())
    client_socket.close()

while True:
    client_sock, address = server.accept()
    print('Conexão recebida de {}:{}'.format(address[0], address[1]))
    client_handler = threading.Thread(
        target=handle_client_connection,
        args=(client_sock,)
    )
    client_handler.start()