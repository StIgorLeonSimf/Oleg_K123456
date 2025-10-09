# i = 0
# while i < 12:
#     i += 1  # i = i + 1
#     if i == 7:
#         continue
#     print(i, end=' ')

# i = 0
# while i < 12:
#     i += 1  # i = i + 1
#     if i == 17:
#         break
#     print(i, end=' ')
# else:
#     print('\nOK')


# n = int(input('> '))
# sm = 0
# cnt = 0
# while n != 0:
#     if n % 2 == 0:
#         sm += n
#         cnt += 1
#     n = int(input('> '))
# print(f'Сумма: {sm}\nКол-во: {cnt}\nСр.арифм.: {sm / cnt}')

""" s = 3 + 2 + 1
    k = 1 + 1 + 1
123 % 10 = 3
    //10 = 12 % 10 = 2
              //10 = 1 % 10 = 1
                         //10 = 0

"""
# n = int(input('> '))
# sn = n
# sm = 0
# k = 0
# while n > 0:
#     m = n % 10
#     sm += m
#     k += 1
#     n //= 10
# print(f'В числе "{sn}" {k} ц. cуммой - {sm}')

# n = int(input('> '))
# res = 0
# while n > 0:
#     m = n % 10
#     res = res * 10 + m
#     n //= 10
# print(res)

# for i in 2, 4, 7, 22:
#     print(i, 'yes')
import sys

# print(list(range(10)))  # Start = 0, Stop, Step = +1
# for i in range(21, 10, -1):
#     print(i, end='  ')

# for i in sys.stdin:
#     print(i)
#     if i.strip() == '0':
#         break

for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i * j:2}', end=' ')
    print()