import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):

    """
    TCP 소켓 연결을 하고 데이터를 입력받는 핸들러
    """
    def handle(self):
        # 클라이언트로부터 1024 byte 크기의 데이터를 읽는다
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)

# myserver.py 가 실행되면 main 함수부터 시작
if __name__ == "__main__":
    # 내부 IP 주소와 포트 설정
    HOST, PORT = "localhost", 8888
    # 외부 IP 주소와 포트 설정
    # HOST, PORT = "210.102.181.108", 8888

    # TCP 서버 소켓을 생성한다
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # ctrl+c 를 누를 때까지 계속 listening 한다 (while 문과 같은 역할)
    server.serve_forever()


