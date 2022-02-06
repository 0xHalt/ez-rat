import time
import sys
import socket
import os

s = socket.socket()
host = "DESKTOP-P3NILB5"
port = 8080
s.connect((host,port))
print("")
print(" Connected to server ")

command = s.recv(1024)
command = command.decode()
if command == "nigger":
    print("")
    print("Shutdown command")
    s.send("command.received".encode())
    os.system("test.txt")
