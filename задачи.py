""" стена 2.5 на 5 метров
рассчитать слои
штукатурка - 5 мешков по 700т руб
финиш - 1 мешок - 700 руб.
краска - банка - 1000 руб.
рассчитать стоимость отдделки стены.

"""

# nm, nm1, *data = 'qwerty', 1, 2, 3, 4, 5, 5
# print(nm, nm1)
# print(data)

"""Про оценки студентов"""
d = {}
name = ''
while name != 'exit':
    name, *marks = input('Имя 4 5 3 4: ').split()
    marks = list(map(int, marks))
    try:
        d[name] = round(sum(marks) / len(marks), 2)
    except ZeroDivisionError:
        break

res = sorted(d.items())
res1 = sorted(d.items(), key=lambda x: x[1], reverse=True)
for i, (k, v) in enumerate(res, 1):
    print(f'{i}. {k} - {v}')
print()
for i, (k, v) in enumerate(res1, 1):
    print(f'{i}. {k} - {v}')