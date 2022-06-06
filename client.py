import threading
import socket


client_name = input('Enter your name :: ')
s = socket.socket()

s.connect((socket.gethostname(), 59000))


def client_response():
    while True:
        try:
            message = s.recv(1024).decode('utf-8')
            if message == "ClientName?":
                s.send(client_name.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error has been occured!")
            s.close()
            break
def client_send():
    while True:
        message = f'{client_name} : {input("")}'
        s.send(message.encode('utf-8'))


response_thread = threading.Thread(target=client_response)
response_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()