num = 5.12

def squaring_1(x):
    sq = x**2
    return sq

def squaring_2(x):
    if len(x):
        squaring_2(x**2)


S1 = squaring_1(num)
print(S1)
S2 = squaring_2(num)
print(S2)
