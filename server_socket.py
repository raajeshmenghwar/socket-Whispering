#/bin/python3
import socket
print('*#'*50)
print("\t\t\t[+] Programmed by rKumar ")
print("\t\t\t[+] Commented  by ChatGPT")
print('*#'*50)  
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('127.0.0.1',5090)) #Active mode

server_socket.listen(10) #Passive mode

print("[+] Listening for connections for 127.0.0.1:5090 ....")

while True:

    conn , addr = server_socket.accept()
    print("[+] Got a connection from {}".format(addr))
     
    while True:
        
        
        data = conn.recv(1024)
        if(data == ''): break
        print("[+] Client sent: ",data.decode())
        
        server_data = input("[+] Enter data to send ")
        conn.send(server_data.encode())
        
    conn.close()
    
