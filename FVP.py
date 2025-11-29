from functools import reduce

ls = [22, 33, 44, 55]
ls1 = [2, 3, 4, 5]
print(ls)

# res = list(map(str, ls))
# res = map(int, ls)
# def power(n):
#     return n ** 2

# res = list(map(power, ls))
# res = list(map(lambda n: n ** 2, ls))
#
# n = 1 if len(ls) > 3 else 100
# print(n)
# res1 = [(lambda n: n ** 2)(i) for i in ls]
# print(res1)
ls = [22, 33, 44, 55]
ls1 = [2, 3, 4, 58, 78]
res = list(map(lambda n, m: n - m, ls, ls1))
# res = list(map(lambda n, m: n > m, ls, ls1))
print(res)
for k, j in zip(ls, ls1):
    print(k - j, end='  ')
print(list(zip(ls, ls1)))

# for i in res:
#     print(i, end=' ')
# print()
# for i in res:
#     print(i, end=' ')
# print()


# res = list(filter(lambda x: x % 2 == 0, ls))
# res1 = [i for i in ls if i % 2 == 0]
# res2 = []
# for i in ls:
#     if i == 'good by':
#         print('yes')
#         break
# print(res)
# print(res1)
# print(res2)

def prim(n, m):
    print('N =', n)
    print('M =', m)
    print('res = ', str(n) + str(m))
    return str(n) + str(m)

city = ['У', 'ф', 'а', '-', 4, 5]

# res = reduce(lambda n, m: str(m) + str(n), city)
res = reduce(prim, city)
print(res)
