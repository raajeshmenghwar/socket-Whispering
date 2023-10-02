#/bin/python3
import socket
print('*#'*50)
print("\t\t\t[+] Programmed by rKumar ")
print("\t\t\t[+] Commented  by ChatGPT")
print('*#'*50)  

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('127.0.0.1',5090))

while True:
    data = input("[+] Enter data to send to Server: ")
    client_socket.send(data.encode())
    
    server_data = client_socket.recv(1024)
    if(server_data == ''): break
    print("[+] Server sent: ", server_data.decode())
    
client_socket.close()
    
    
