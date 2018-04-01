import socket
import sys
import time
import random

#HOST, PORT = "localhost", 8888
HOST, PORT = "192.9.81.104", 8888


def getRandomData():
    random_data = ""
    for i in range(4):
        random_data = random_data + str(random.randint(0, 10))
        if i < 3:
            random_data = random_data + "_"
    return random_data

def main():
    # 매 1ms 마다 데이터를 무작위로 생성해서 보낸다 
    # while True:
    for i in range(60000):
        # Create a socket (SOCK_STREAM means a TCP socket)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            # Connect to server and send data
            sock.connect((HOST, PORT))
            data = getRandomData()
            sock.sendall(bytes(data + "\n", "utf-8"))

            # Receive data from the server and shut down
            received = str(sock.recv(1024), "utf-8")
        finally:
            sock.close()
        print("Sent:     {}".format(data))
        if received is "":
            print("Received: NULL")
        else:
            print("Received: {}".format(received))
        time.sleep(0.001)


if __name__ == "__main__":
   main() 
