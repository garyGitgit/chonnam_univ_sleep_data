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
        data_len = len(data)
        decimals = []
        # 10진수로 바꿔서 저장
        for i, d in enumerate(data):
          if i == 0 or i == data_len-1:
            pass
          else:
            decimals.append(int("0x"+data[i],16))
    	    
        # db 연결
        conn = sqlite3.connect('db/sleep_data.db')
        print ("Opened database successfully")
        # db 저장 
        insert_cmd = "INSERT INTO SLEEP_DATA (USERNAME, DATA_A, DATA_B, DATA_C, DATA_D, DATA_E, DATA_F, CREATED_DATE) VALUES("+"'"+name+"',"+str(decimals[0])+","+str(decimals[1])+","+str(decimals[2])+","+str(decimals[3])+","+str(decimals[4])+","+str(decimals[5])+","+timestamp+")"
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
