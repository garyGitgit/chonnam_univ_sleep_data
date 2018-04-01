import socket
import sys
import time

HOST, PORT = "localhost", 8888

# Create a socket (SOCK_STREAM means a TCP socket)

while True:
  
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # Connect to server and send data   
  sock.connect((HOST, PORT))
  sock.send(bytes("client1", 'utf-8'))
  time.sleep(1)
  sock.close()

