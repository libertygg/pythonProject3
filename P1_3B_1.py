from random import randint

lst1 = []
for i in range(10):
    lst1.append(randint(1, 100))

nxt1 = iter(lst1)

lst2 = []

for i in range(10):
    nxt2 = next(nxt1)
    if nxt2 >= 40:
        lst2.append('High')
    else:
        lst2.append('Low')

print(lst1)
print(lst2)

