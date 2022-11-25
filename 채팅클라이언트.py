import socket
import threading #스레드 모듈

ip = "localhost"
port = 50001

#데이터 수신 함수
def receive(client_socket):
    state = True

    while True:
        #예외처리
        try:
             #메세지 수신
            message = client_socket.recv(1024).decode("UTF-8")

            #메세지 출력
            if state:
                print(message, end='')
                state=False
            else:
                print(message)

                    
        except Exception as error:
            print("에러발생",error)
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    #서버와 연결
    client_socket.connect((ip,port))

    #서브 스레드 객체 생성
    thread = threading.Thread(target=receive, args=(client_socket,))
    thread.daemon = True # 스레드를 생성한 메인 스레드가 종료되면 같이 종료
    thread.start() #스레드 시작

    print('[Enter 입력시 시작]')

    while True:
        #서버로 메세지 전송
        message = input().encode("UTF-8")

        client_socket.send(message)
        
        #퇴장기능
        if message == "/exit":
            break

