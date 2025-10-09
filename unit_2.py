"""
+, -, *, **, /, //, %
"""
from math import sqrt

a = 31
b = 45
c = 57

"""
p = (a+b+c)/2
s = sqrt(p(p-a)(p-b)(p-c))
"""
p = (a + b + c) / 2
s = sqrt(p * (p - a) * (p - b) * (p - c))
print('Площадь = "', round(s, 2), '"', sep='')
f1 = 'Площадь = "{}"'.format(round(s, 2))
f = f'Площадь = "{s:.2f}"'
print(f1)
print(f)
print(f'Площадь = "{s:.3f}"')