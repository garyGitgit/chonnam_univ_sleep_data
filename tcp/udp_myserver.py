import socket 
import sqlite3

#HOST = "210.102.181.108"
# 이 IP 는 내부 네트워크 IP 
HOST = "192.9.81.104"
PORT = 8080

# 소켓 생성 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((HOST, PORT))

# db 연결 



# 이 IP 에 대해서는 bind 할 수 없다고 나오네 (외부 IP 는 필요가 없다? router 가 알아서 해준다?

# 데이터 받을 크기를 byte 단위로 입력한다 : 500byte
print("server is listening...")
# 데이터 수신 대기
while 1:
  # 소켓을 통해서 데이터를 받음 
  recv_data = s.recv(500) 
  print ("server", recv_data)
  # byte 로 들어온 데이터 디코딩한 후 underscore 기준으로 파싱
  data = recv_data.decode("utf-8").split('_')

  name = data[0] 
  timestamp = data[-1]
  # db 연결
  conn = sqlite3.connect('db/sleep_data.db')
  print ("Opened database successfully")
  # db 저장 
  insert_cmd = "INSERT INTO SLEEP_DATA (USERNAME, DATA_A, DATA_B, DATA_C, DATA_D, DATA_E, DATA_F, CREATED_DATE) VALUES("+"'"+name+"',"+str(data[1])+","+str(data[2])+","+str(data[3])+","+str(data[4])+","+str(data[5])+","+str(data[6])+","+str(data[7])+")" 
  print(insert_cmd)
  conn.execute(insert_cmd);
  conn.commit()
  print ("Records created successfully")
  conn.close()



