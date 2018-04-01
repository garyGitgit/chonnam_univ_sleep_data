import socketserver
import sqlite3

class MyTCPHandler(socketserver.StreamRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.rfile.readline().strip()
        f.write(str(self.data)+'\n')
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)


        # byte 로 들어온 데이터 디코딩한 후 underscore 기준으로 파싱
        data = self.data.decode("utf-8")
        starttime = 0
        if (data.startswith('DEV:')) : 
            DEV = data.split('DEV:')[1].split(',')[0] #DEV 값 저장
            starttime = data.split('StartTime:')[1].split('\n\r')[0] #StartTime 값 저장
            print(DEV, starttime)

        else : 
            # underscore 기준으로 data 파싱
            #data = self.data.decode("utf-8").split('_')

            data = self.data.decode("utf-8").split('\n\r')
            data = data.split('_')

            print(data)
            #Text 형식으로 저장하기에 일단 주석처리
            data_len = len(data)
            decimals = []

            # 10진수로 바꿔서 저장
            #for i, d in enumerate(data):
                #if i == 0 or i == data_len-1:
                    #pass
                #else:
                    #decimals.append(int("0x"+data[i],16))
    	    
            # db 연결
            conn = sqlite3.connect('db/sleep_data.db')
            print ("Opened database successfully")

            # db 저장 
            insert_cmd = "INSERT INTO SLEEP_DATA (Name, time, ch1, ch2, realtime) VALUES('%s', '%s', '%s', '%s', '%s')" % (data[0], data[1], data[2], data[3], starttime)
            print(insert_cmd)
            conn.execute(insert_cmd);
            conn.commit()
            #self.request.send(b"success") #테스트 응답 값
            print ("Records created successfully")
            conn.close()

            #starttime = (starttime) + int(data[1])

if __name__ == "__main__":
    HOST, PORT = "192.9.81.104", 8888 
    f = open("log.txt", 'w')
    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
    f.close()
