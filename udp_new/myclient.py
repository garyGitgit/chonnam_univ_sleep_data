import socket
import time
 
# 서버의 IP 주소 
# HOST = "192.9.81.104" 
HOST = "0.0.0.0" 
# 서버의 포트 주소
PORT = 8080
# 전송할 데이터
data = "Ah_92111220_11_22\n\r"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# UDP 전송 
while 1:
  s.sendto(data.encode("utf-8"), (HOST, PORT))
  print ("client : data sent!")
  # 1초동안 sleep 한다	
  time.sleep(1)






