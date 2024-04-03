# 인터럽트 예제  
import time # 시간을 처리하기 위한 패키지

import signal # 비동기 처리를 위한 패키지


def handler(signum, frame): # 인터럽트를 처리하는 함수
    print('키보드 인터럽트 감지!')
    print('신호 번호:', signum)
    print('스택 프레임:', frame)
    exit()

signal.signal(signal.SIGINT, handler) # 인터럽트를 처리하는 함수를 등록

while True:
    print('5초 간격으로 출력 중...')
    time.sleep(5)