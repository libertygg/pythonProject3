nums = [12.22,-1.83,3,-45.43,31,12,14,-12,67,-3,0,53.12,-193]
s_nums = sorted(nums)

def func_1(x):
    p_nums = []
    n_nums = []
    for i in x:
        if i >= 0:
            p_nums.append(i)
        if i < 0:
            n_nums.append(i)
    tup = sorted(p_nums), sorted(n_nums)
    return tup
"""Создание, наполнение списков соответствующими условиям числами; 
создание на основе списков кортежа из двух списков"""

N = func_1(s_nums)
print(N)