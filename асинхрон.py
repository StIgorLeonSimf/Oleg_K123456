import asyncio
import time


# def f1(n):
#     print(n ** 2)
#     time.sleep(3)
#     print('F1 copleted')
#
#
# def f2(n):
#     print(n * 5)
#     time.sleep(3)
#     print('F2 copleted')
#
#
# def main():
#     f1(5)
#     f2(100)


# if __name__ == '__main__':
#     start = time.perf_counter()
#     main()
#     stop = time.perf_counter()
#     print(f'Время выполнения {stop - start}')

async def f1(n):
    print(n ** 2)
    await asyncio.sleep(3)
    print('F1 copleted')


async def f2(n):
    print(n * 5)
    await asyncio.sleep(2)
    print('F2 copleted')


async def main():
    task1 = asyncio.create_task(f1(5))
    task2 = asyncio.create_task(f2(100))
    await task1
    await task2


if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    stop = time.perf_counter()
    print(f'Время выполнения {stop - start:.1f} cек.')