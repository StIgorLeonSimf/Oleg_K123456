# def name(x, y):
#     print('YEs')
#     print(x * 10 + y * 100)
#     # return x * 10 + y * 100


# def coffee(name, cost):
#     names = ['Tea', 'Cacao', 'Americano']
#     costs = [60, 80, 100]
#     if name in names:
#         ind = names.index(name)
#         cost_name = costs[ind]
#         if cost_name == cost:
#             print(f'Ваш {name} готовится!')
#             return name
#
#
# # hand = coffee('Cacao', 80)
# # print(hand)
#
# # nn = name(2, 5)
# # print(nn)
#
#
# def summator(x=50, y=20):
#     global z
#     f = 100
#     z += 1
#     print('z Func =', z)
#     return x + y
#
#
# #
# # z = 23
# # print(summator(10, 16))
# # n = summator(y=100)
# # print('n =', n)
# # print(z)
#
#
# def is_even(n: int) -> bool:
#     return n % 2 == 0
#
#
# def choice_even(x, y):
#     for i in range(x, y + 1):
#         if is_even(i):
#             print(i, end=' ')
#     print()
#
#
# # choice_even(100, 140)
# # def num2(n):
# #     if n > 1:
# #         num1(n-1)
# #     print(n)
# #
# #
# # def num1(n):
# #     if n > 1:
# #         num2(n-1)
# #     print(n)
#
# def num(m, n):
#     if n > m:
#         num(m, n - 1)
#     print(n)
#
#
# # num(7, 11)
#
# l = [1, 2, [3, 4, [5.5, 6, [7, [8]]]]]
# def sumer(ls):
#     res = 0
#     for i in ls:
#         if type(i) != list:
#             res += i
#         else:
#             res += sumer(i)
#     return res
#
# # print(sumer(l))
#
# """
# 0 1 1 2 3 5 8 13 21 34 55  ......
#
# n(f) = (n-1)(f) + (n-2)(f)
# """
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
# print(fib(2))

"""
3! = 1 * 2 * 3 = 3 * 2!
2! = 1 * 2     = 2 * 1!
1! = 1
n! = n * (n-1)!
"""

def name(nm):
    cnt = 0
    def surname(snm):
        nonlocal cnt
        cnt += 1
        print(cnt, nm, snm)
    return surname

cnt = 1000
sur = name('Marry')
sur('Petrova')
sur('Ivanova')
sur('Sidorova')