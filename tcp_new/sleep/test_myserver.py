import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    TCP 서버 측에서 Stream으로 들어오는 것을 임의로 자르기 때문에 클라이언트가 보내는 형식은 중요하지않음
    """
    def handle(self):
        str_data = ""
        print("str data : ", str_data)
        # self.request is the TCP socket connected to the client
        print("handling..........")
        data = self.request.recv(4096).strip()
        str_data = str_data + data.decode("utf-8")
        print("received data : ", str_data)
        
        print("-----------------------------")
        isParsing = True 
        while isParsing:
          result  = str_data.split("\n\r", 1)
          print(result[0])
          if len(result) > 1:
            str_data = result[1]
          else:
            str_data = result[0]
            isParsing = False
            # conn.execute (쿼리 날리기)
        #conn.commit (쿼리 커밋) 
            
          

        # just send back the same data, but upper-cased
        #self.request.sendall(self.data.upper())


if __name__ == "__main__":
    HOST, PORT = "192.9.81.104", 8888 

    # Create the server, binding to localhost on port 8888
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
