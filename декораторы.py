import random
import time


def time_run(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        stop = time.perf_counter()
        duration = stop - start
        print(f'Время работы функции {func.__name__} - {duration:.2f} сек.')
    return wrapper


def in_out(func):
    def wrapper(*args, **kwargs):
        print(f'Функция {func.__name__} принимает - {args}, {kwargs}')
        res = func(*args, **kwargs)
        print(f'Функция {func.__name__} возвращает - {res}')
        return res
    return wrapper


def decor(func):
    def wrapper():
        print('Before')
        func()
        print('After')

    return wrapper


def inside(a, b, c, x=1, y=2):
    print(a, b, c, x, y)


# @decor
def proba(*args, **kwargs):
    print(args)
    print(kwargs)
    inside(*args, **kwargs)

@time_run
def etalon(n, m):
    print('START')
    time.sleep(n + m)
    print('STOP')


@in_out
def sumr(x, y):
    return x + y


# proba(1, 4, 5, x=25, y=54)
# inside(11, 12, 13, 14, 15)
# decor(proba)()
# etalon(3, 1)


# n, *dig = 1, 2, 3
# print(n, *dig)
# print(n, dig)

res = 1.3547 * sumr(random.randint(10, 100), random.randint(10, 100)) / .47 + 80
print(res)