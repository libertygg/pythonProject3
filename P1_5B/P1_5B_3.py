def squaring(x,y):
    sq = x**y
    return sq
"""Возведение в степень."""
def squaring_rec(x,y):
    if y == 1:
        return(x)
    if y != 1:
        sq_rec = x * squaring_rec(x, y-1)
        return sq_rec
"""Возведение в степень с использованием рекурсии."""

num = 5.12
y = 2

S1 = squaring(num,y)
print(S1)
S2 = squaring_rec(num,y)
print(S2)
