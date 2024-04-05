from multiprocessing import Process
import os
import time

def writer():
    print(f'{os.getpid()}가 파일에 쓴다')
    with open('13-test.txt', 'w') as f:
        f.write('Hello, world!')


def roader():
    print(f'{os.getpid()}가 파일을 읽는다')
    with open('13-test.txt', 'r') as f:
        print(f.read())

if __name__ == '__main__':
    p1 = Process(target=writer)
    p1.start()

    time.sleep(2)

    p2 = Process(target=roader)
    p2.start()

    p1.join()
    p2.join()  