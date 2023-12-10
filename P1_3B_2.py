import names
from random import randint

first_names = []
for i in range(100):
    first_names.append(names.get_first_name())

lstAM = ['A','B','C','D','E','F','G','H','I','J','K','L','M']

first_letters = []
it = iter(first_names)

J = 0
while J != 100:
    J += 1
    it2 = next(it)
    first_letters.append(it2[0])

top_list = zip(first_letters, first_names)

YT = iter(top_list)

lst_names_AM = []
lst_names_NZ = []
for H in range(100):
    YT2 = next(YT)
    if YT2[0] in lstAM:
        lst_names_AM.append(YT2)
    else:
        lst_names_NZ.append(YT2)

NamesAM = []
GG1 = iter(lst_names_AM)

for i in range(len(lst_names_AM)):
    GG2 = next(GG1)
    NamesAM.append(GG2[1])

NamesNZ = []
GG3 = iter(lst_names_NZ)

for i in range(len(lst_names_NZ)):
    GG4 = next(GG3)
    NamesNZ.append(GG4[1])

print('Имена от A до M:')
print(NamesAM[0:16])
print(NamesAM[16:])
print('Имена от N до Z:')
print(NamesNZ[0:16])
print(NamesNZ[16:])



