import threading
import socket


HOST = '10.19.49.126'
PORT = 50000


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(5)


clients = []
client_names = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            client_name = client_names[index]
            broadcast(f'{client_name} has left the chat server'.encode("utf-8"))
            client_names.remove(client_name)
            break

def client_connection():
    while True:
        print('Server is running and listenning.....')
        client_socket, address = s.accept()
        print(f'Connection is established with {str(address)}')
        client_socket.send('Client Name ?'.encode("utf-8"))
        client_name = client_socket.recv(1024)
        client_names.append(client_name)
        print(f'The recent client is {client_name}'.encode('utf-8'))
        broadcast(f'{client_name} has connected to the chat server'.encode('utf-8'))
        client_socket.send('You are now connected!'.encode('utf-8'))

        thread = threading.Thread(target=handle_client,args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    client_connection()