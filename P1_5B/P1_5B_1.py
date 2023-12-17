def clean(x):
    clear_reg = list(filter(None, x))
    return clear_reg
"""Приведение данных к единому, поддающемуся вычислению, формату."""

def middle_temp(y):
    mt = sum(y) / len(y)
    return mt
"""Вычисление среднего значения."""

register = [12,14,15,None,16,14,None,12,None,10,9]
y = clean(register)
h = middle_temp(y)

print(h)







