import socketserver
import readline
import os

class MyTCPHandler(socketserver.BaseRequestHandler):


	def handle(self):
		print("TCP connection complete!!!")
		f = open("new_file.txt", "a")

		while True :
			# 1024바이트씩 받아서
			sock = self.request.recv(1024)
			# encoding해주고
			data = str(sock, encoding='utf-8')
			
			if '\n\r' in data : 
				data = data.replace("\n\r", "\n")

	
			f.write(data)

			#break 지점 추가해야함
		f.close()


if __name__ == "__main__":
	HOST, PORT = "192.9.81.104", 8888 

	# Create the server, binding to localhost on port 8888
	server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

	# Activate the server; this will keep running until you
	# interrupt the program with Ctrl-C
	server.serve_forever()
