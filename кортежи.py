"""tuple"""

tp = (22, 33, 44)
# print(len(tp))
# for i in tp:
#     print(i)

x, y, z = 6, 8, 2
print(x, y)

# 2
"""def modify_lastelement(tp_tuple, k):
    pass

mytuple1 =(1, 1, 2)
mytuple2 = (2, 4)
tpl_tuple = (mytuple1, mytuple2)
mylist2 = modify_lastelement(tpl_tuple, 5)"""
tp = ('login', 'password')
buff = list(tp)
buff[-1] = '12345'
print(buff)
print(tp)
tp = tuple(buff)
print(tp)

