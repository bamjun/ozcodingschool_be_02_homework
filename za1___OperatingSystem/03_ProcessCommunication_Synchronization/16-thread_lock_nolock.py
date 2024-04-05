import threading
from multiprocessing import Value

def counter1(snum, cnt):
    try:
        for i in range(cnt):
            snum.value += 1
    finally:
        print('counter1 done ')


def counter2(snum, cnt):
    try:
        for i in range(cnt):
            snum.value -= 1
    finally:
        print('counter2 done ')


if __name__ == '__main__':
    shared_number = Value('i', 0)
    t1 = threading.Thread(target=counter1, args=(shared_number, 40000))
    t1.start()

    t2 = threading.Thread(target=counter2, args=(shared_number, 40000))
    t2.start()

    t1.join()
    t2.join()

    print(shared_number.value)