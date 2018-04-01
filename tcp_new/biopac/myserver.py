import socketserver
import sqlite3

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
          # byte 로 들어온 데이터 디코딩한 후 underscore 기준으로 파싱
        data = self.data.decode("utf-8").split('_')

        name = data[0]
        timestamp = data[-1]
        # db 연결
        conn = sqlite3.connect('db/biopac_data.db')
        print ("Opened database successfully")
        # db 저장 
        insert_cmd = "INSERT INTO BIOPAC_DATA (USERNAME, BARO, RED, GREEN, BLUE, IR, AMB1, AMB2, BIOPAC, CREATED_DATE) VALUES("+"'"+name+"',"+str(data[1])+","+str(data[2])+","+str(data[3])+","+str(data[4])+","+str(data[5])+","+str(data[6])+","+str(data[7])+","+data[8]+","+timestamp+")"
        print(insert_cmd)
        conn.execute(insert_cmd);
        conn.commit()
        print ("Records created successfully")
        conn.close()

        # just send back the same data, but upper-cased
        # self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "192.9.81.104", 8888

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
