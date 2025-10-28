import time
from threading import Thread


def f1(n):
    print(n ** 2)
    time.sleep(3)
    print('f1 работу закончила')


def f2(n):
    print(n * 5)
    time.sleep(2)
    print('f2 работу закончила')



thread1 = Thread(target=f1, args=(5,))
thread2 = Thread(target=f2, args=(100,))

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print('base thread Comleted')