import socket
import sys

#HOST, PORT = "localhost", 8888
#HOST, PORT = "210.102.181.108", 8888
HOST, PORT = "192.9.81.104", 8888
data = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    data = b"e8c_01_002d_002a\n\re8c_01_0416_0501\n\re8c_01_082c_0974\n\re8c_01_0adc_0c2a\n\re8c_01"
    sock.sendall(data)
finally:
    sock.close()
