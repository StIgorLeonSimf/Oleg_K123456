s = 'ЗдраВствуйте, гости!'

# for i in s:
#     print(i, end='  ')
print(s[-1])
print(s[:12])

print(s.isalpha())
s1 = '1234a'
print(s1.isdigit())
print(s1.isalnum())
print(s.islower())
print(s.isupper())
print(s.startswith('ЗдрA'))
print(s.endswith('!'))

# new = s.upper()
print(s.lower())
print(s.upper())
print(s.capitalize())
print(s.title())
print(s.rjust(80))
print(s.ljust(80))
print(s.center(80))
print(s.strip())
print(s.strip('!ит З'))
print(s.rstrip())
print(s.lstrip())
print(s.find('т', 11, 15))
print(s.count('т'))
print(s.replace('т', 'Т', 2).replace(' ', ''))
l = s.split(', ')
print(l)

a = 'I like python, it is very useful for data analysis'
b = 'python is the best tool for dealing with big data'
# выписать вторую строку без слов в первой строке