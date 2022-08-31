tup1 = (1, 2, 3, 5)

print(id(tup1))
l1 = list(tup1)
l1[3] = 4
tup1 = tuple(l1)
print(tup1)
print(id(tup1))
