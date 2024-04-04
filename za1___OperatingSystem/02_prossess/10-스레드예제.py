import threading
import os
import time

def something(word):
    while True:
        print(word)
        time.sleep(3)

if __name__ == '__main__':
    print('기존 프로세스 아이디:', os.getpid())
    thread1 = threading.Thread(target=something, args=('happy',))
    thread1.daemon = True
    thread1.start()
    print('메인 스레드에서 반복문 시작')
    while True:
        try:
            print('daily...')
            time.sleep(3)
        except KeyboardInterrupt:
            print('good bye~')
            break