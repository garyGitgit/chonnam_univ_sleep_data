import socket 
import sqlite3
import datetime
import os

def create_newfile(device_id):
  print("new file created")
  #yymmddhhmm.LOG 파일 생성 
  now = datetime.datetime.now()
  print(now)
  year = str(now.year)[2:]
  month = str(now.month)
  if len(month) == 1:
    month = "0" + month
  day = str(now.day)
  if len(day) == 1:
    day = "0" + day
  hour = str(now.hour)
  if len(hour) == 1:
    hour = "0" + hour
  minute = str(now.minute)
  if len(minute) == 1:
    minute = "0" + minute
  filename = year + month + day + hour + minute + ".LOG"

  second = str(now.second)
  if len(second) == 1:
    minute = "0" + second

  f = open(filename, "w")
  # 첫 줄에 파일 생성 날짜와 디바이스 이름을 적는다 
  start_line = device_id + " / CreatedTime:" + year + month + day + "_" + hour + minute + second + "\n"
  f.write(start_line)
  f.close()

  # meta.txt 에 기록한다 
  f = open("meta.txt", "w+")
  f.write(filename+"\n")
  return filename

def isFileFull(filename):

  # 크기를 비교한다 
  file_size = os.path.getsize(filename)
  file_size_mb = file_size/(1024*1024.0)
  if file_size_mb >= 8:
    print("file size is full")
    return True
  else:
    return False

#localhost 로 테스트 
#HOST = "localhost"

#HOST = "210.102.181.108"

# 이 IP 는 내부 네트워크 IP 
#HOST = "192.9.81.104"
HOST = "0.0.0.0"
PORT = 8080
 
# 소켓 생성 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
s.bind((HOST, PORT))
 
 
# 이 IP 에 대해서는 bind 할 수 없다고 나오네 (외부 IP 는 필요가 없다? router 가 알아서 해준다?
 
# 데이터 받을 크기를 byte 단위로 입력한다 : 500byte
print("server is listening...")
# 데이터 수신 대기

# file open
# 메타데이터 파일을 읽어서 가장 최근 파일을 읽는다 
current_filename = ""
for line in reversed(list(open("meta.txt"))):
    current_filename = line[:-1]
    break

# 첫 파일 생성 
# if current_filename == "":
#   current_filename = create_newfile()
#   print(current_filename)
# # 가장 최근 저장된 파일이 있는 경우
# else :
#   # 8MB 이상이면
#   #새 파일을 생성한다 
#   if isFileFull(current_filename[:-1]):
#     current_filename = create_newfile()
print(current_filename)

while 1:
  # 소켓을 통해서 500byte 단위로 데이터를 받음 
  recv_data = s.recv(500) 
  print ("SERVER received data : ", recv_data)
  # byte 로 들어온 데이터 디코딩한 후 underscore 기준으로 파싱
  data = recv_data.decode("utf-8").split('_')

  # 데이터 파싱해서 하나의 line 으로 만듦
  line = data[0] + ", " + data[1] + ", " + data[2] + ", " + data[3]

  # 매번 8MB 가 되었는지 확인한다 / 만약에 8MB가 됐으면 새로운 파일을 생성한다 
  if current_filename == "" or isFileFull(current_filename):
    current_filename = create_newfile(data[0])
 

  # 파일을 계속 open, close 하는게 무리가 있지 않을까 걱정이지만 일단은 이렇게 한다 

  # 데이터 파일에 저장
  file = open(current_filename, "a")
  file.write(line)
  file.close()

  
  # 이전 코드 
  # name = data[0] 
  # timestamp = data[-1]
  # # db 연결
  # conn = sqlite3.connect('db/sleep_data.db')
  # print ("Opened database successfully")
  # # db 저장, 들어오는 데이터는 Device, time, ch1, ch2의 형식
  # insert_cmd = "INSERT INTO SLEEP_DATA (Name, Device, ch1,ch2) VALUES("+"'"+name+"',"+str(data[1])+","+str(data[2])+","+str(data[3])+")" 
  # print(insert_cmd)
  # conn.execute(insert_cmd);
  # conn.commit()
  # print ("Records created successfully")
  # conn.close()



# while 1:
#   # 소켓을 통해서 500byte 단위로 데이터를 받음 
#   recv_data = s.recv(500) 
#   print ("server", recv_data)
  # byte 로 들어온 데이터 디코딩한 후 underscore 기준으로 파싱
  # data = recv_data.decode("utf-8").split('_')
 
  # name = data[0] 
  # timestamp = data[-1]
  # # db 연결
  # conn = sqlite3.connect('db/sleep_data.db')
  # print ("Opened database successfully")
  # # db 저장, 들어오는 데이터는 Device, time, ch1, ch2의 형식
  # insert_cmd = "INSERT INTO SLEEP_DATA (Name, Device, ch1,ch2) VALUES("+"'"+name+"',"+str(data[1])+","+str(data[2])+","+str(data[3])+")" 
  # print(insert_cmd)
  # conn.execute(insert_cmd);
  # conn.commit()
  # print ("Records created successfully")
  # conn.close()





