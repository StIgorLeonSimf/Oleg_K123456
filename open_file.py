# file = open('text.txt', 'r', encoding='utf-8')
# # s = file.read(10)
# # print(s)
# # s1 = file.readline()
# # print(s1)
# ls1 = file.readlines()
# print(ls1)
# file.close()

# for i in open('text.txt', 'r', encoding='utf-8'):
#     print(i.strip())

# with open('text.txt', 'r', encoding='utf-8') as file:
#     s = file.read()
# print(s)

# получить нормальный список фамилий
with open('text.txt', 'r', encoding='utf-8') as file:
    ls = file.read().title().split()
    ls.sort()
print(ls)
with open('text1.txt', 'w', encoding='utf-8') as file:
    for n, i in enumerate(ls, 1):
        print(f'{n}. {i}')
        file.write(f'{n}. {i}\n')