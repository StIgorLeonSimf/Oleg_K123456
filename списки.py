"""list"""
import copy
import random

"""    0   1   2   3   4   """
l = [55, 55, 44, 55, 99]
"""   -5  -4  -3  -2  -1   """

# ls[0] = 220
print(l[4])
print(l[-1])
print(l)
print(l[2:])
print(l[2::-1])
print(l[::-1])
# l1 = l[:]
# l = [1, 2, [3, 4]]
# l1 = l
l1 = l.copy()
# l1 = copy.deepcopy(l)
# print(id(l))
# print(id(l1))
# l[1] = 200
# l[-1][-1] = 400
# print(l)
# print(l1)
print(len(l))
l.append(100)  # O(1)
l.insert(0, 200)  # O(n)
# l.extend([1, 2])
# l += [1, 2]
x = l.pop()  # O(1)
y = l.pop(0)  # O(n)
print(l)
# while 55 in l:
#     l.remove(55)
print(x, y)

print(l.count(55))
print(l.index(55, 1, 10))
l.reverse()
l.sort(reverse=True)
print(l)
names = ['Mary', 'Cherry', 'Berry', 'Terry']
names.sort(key=lambda x: len(x))
print(names)

for i in range(len(names)):
    print(i, names[i], end=' ')
print()

cnt = 0
for i in names:
    print(cnt, i, end=' ')
    cnt += 1
print()

for k, i in enumerate(names):
    print(k, i)

for k, i, j in zip(l, l1, l):
    print(k + i + j)

# n, m = 0, 'Mary'
# print(n, m)

arr = [0] * 10
# arr[0] = 12
for i in range(len(arr)):
    arr[i] = i ** 2
print(arr)

print(random.random())
print(random.uniform(10, 21))

print(random.randint(11, 12))
print(random.randrange(2, 20, 2))

print(random.choice(names))

print(random.choices(names, k=7))
names = ['Mary', 'Cherry', 'Berry', 'Terry', 'Very']
ages = [19, 23, 20, 21, 24]
gender = ['f', 'f', 'm', 'm', 'f']
print(random.sample(names, 3))

for k, i in enumerate(names, 1):
    print(f'{k}. {i}')

cnt = 1
for i in names:
    print(f'{cnt}. {i}')
    cnt += 1
lst = []
for i in zip(names, ages, gender):
    lst.append(i)
print(lst)