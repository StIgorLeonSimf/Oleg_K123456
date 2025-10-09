"""set"""
# """    1   8  10 12  20  21 30 37 """
st = {21, 22, 33, 22}
l = []
st_free = set()
print(st_free)
# st = set(l)
st.add(100)
st.update({1})

n = st.pop()
st.remove(22)
st.discard(21)
print(n)
print(st)
# st1 = st.copy()
st1 = {1, 2, 33}
st2 = {1, 2, 44}

# res = st1.union(st2)
# res = st1 | st2

# res = st1.intersection(st2)
# res = st1 & st2

# res = st1.difference(st2)
# res = st1 - st2
# st1.difference_update(st2)

# res = st1.symmetric_difference(st2)
res = st1 ^ st2
print(res)

st1 = {1, 2, 33}
st2 = {1, 2, 44}
st3 = {1, 2}
print(st3.issubset(st2))
print(st2.issuperset(st3))