import socketserver
import sqlite3

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    요청을 기다리다가 클라이언트에게서 접속 요청(Socket.connect())이 오면 이를 수락한 뒤 BaseRequestHandler 객체의 handle() 메소드 호출
    TCP 서버 측에서 Stream으로 들어오는 것을 임의로 자르기 때문에 클라이언트가 보내는 형식은 중요하지않음
    """
    def handle(self):
        str_data = ""
        starttime = 0
        # self.request is the TCP socket connected to the client


        data_count = 0
        while True:

            print("handling..........")

            data = self.request.recv(1024).strip()
            str_data = str_data + data.decode("utf-8")

            # db 연결
            print("DB 연결 전")
            conn = sqlite3.connect('db/sleep_data_v1.db')
            print ("Opened database successfully")
            print("-----------------------------")

            isParsing = True 
            while isParsing:
              result  = str_data.split('\n\r', 1)

              if len(result) > 1:  #정상적인 데이터
                str_data = result[1]
                #StartTime, Dev
                if (result[0].startswith('DEV:')) : 
                  DEV = result[0].split(', ')[0].split('DEV:')[1] #DEV 값 저장
                  if 'StartTime:' or 'MidTime:' :
                    starttime = result[0].split(', ')[1].split('StartTime:')[1] #StartTime 값 저장
                    starttime = result[0].split(', ')[1].split('MidTime????쉬벌')[1] #MidTime 값을 starttime값에 저장

                else :
                  print("Else문에 들어왔음")

                  # underscore 기준으로 data 파싱
                  n_data = result[0].split('_')
               
                  # db 저장 
                  insert_cmd = "INSERT INTO SLEEP_DATA_TABLE (Name, time, ch1, ch2, realtime) VALUES('%s', '%s', '%s', '%s', '%s')" % (n_data[0], n_data[1], n_data[2], n_data[3], starttime)
                  print(insert_cmd)
                  conn.execute(insert_cmd)
                  print ("Records created successfully")
              else:
                str_data = result[0]
                print("한 줄 데이터 : ", str_data)
                isParsing = False

            conn.commit()
            conn.close()
          

if __name__ == "__main__":
    HOST, PORT = "192.9.81.104", 8888 

    # Create the server, binding to localhost on port 8888
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
