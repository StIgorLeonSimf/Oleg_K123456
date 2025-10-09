"""dict"""

# d = {}
st = {'Pb', 'Au'}
d = {'Pb': 'свинец',
     'Au': 'Золото'
     }
print(d['Pb'])
print(d.get('Pb2', 'no key'))

d['Pb'] = 'Свинец'

d[10] = 111
d.setdefault(2, 22)
d.update({3: 33, 10: 11})

n = d.pop(2)
n1 = d.popitem()
print(n)
print(n1)
print(d)

print(list(d))
print(list(d.values()))
print(list(d.items()))

for k in d:
     print(k, end=' ')
print()
for v in d.values():
     print(v, end=' ')
print()
for k, v in d.items():
     print(k, v, end='     ')
print()


# l = [22, 33, 44, 44]
# dd = dict.fromkeys(l, 1000)
# tp = ((12, 1212), (15, 1515), (20, 222))
# dd = dict(tp)
# dd = {}
# for i in range(10, 20):
#      dd[i] = i ** 2

# dd = {i: i ** 2 for i in range(10, 20)}
# print(dd)

s = 'aaaaaaaaaabaaaaaaacaaaaaaaaabaaaaaaaacaaaaaaaabaaaaaaaaaaacaaaaaaaaaac'
# name = []
# count = []
# d = {}
# cnt = 0
# count_a = 0
# for i in set(s):
#      # cnt += 1
#      # name.append(i)
#      # count.append(s.count(i))
#      d[i] = s.count(i)
#
#
#
# # print(name)
# # print(count)
# # for k, v in zip(name, count):
# #      print(f'{k}:- {v}', end=' ..... ')
# # print()
# #
# # print(d)
# s = 'iiiiiii iiiiaaaaa iiiqweerty asdhgf iii'
# res = s.split()
# l = []
# for i in res:
#      if 'iii' == i:
#           l.append(i)
# print(l)
#
#
