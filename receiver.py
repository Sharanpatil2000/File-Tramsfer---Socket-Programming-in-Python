import os
import socket
import time
host = input("Host Name: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
 sock.connect((host, 22222))
 print("Connected Successfully")
except:
 print("Unable to connect")
 exit(0)

file_name = sock.recv(100).decode()
file_size = sock.recv(100).decode()

with open("./rec/" + file_name, "wb") as file:
 c = 0

 start_time = time.time()

 while c <= int(file_size):
 data = sock.recv(1024)
 if not (data):
 break
 file.write(data)
 c += len(data)

 end_time = time.time()
print("File transfer Complete.Total time: ", end_time - start_time)

sock.close()