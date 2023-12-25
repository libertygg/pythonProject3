from random import randint

def comp_numb():
    n_comp = randint(1, 100)
    print(n_comp)
    print('Компьютер "загадал" число в интервале от 1 до 100. Какое?')
    return n_comp

def attempt(func):
    def numb_of_attempt(u_n, c_n, nf):
        global n
        nf += 1
        n = nf
        return_value = func(u_n, c_n, nf)
        return return_value
    return numb_of_attempt

@attempt
def check_numder(u_n, c_n, nf):
    print("Попытка:", nf)
    if u_n > c_n:
        return 'Загаданное число меньше'
    elif u_n < c_n:
        return 'Загаданное число больше.'
    else:
        return "Правильно! Число попыток отгадывания:", nf
    return return_value

def us_numb():
    while True:
        x = int(input('Введите Ваше число: '))
        return x

c_n = comp_numb()
u_n = 0
n = 0
while c_n != u_n:

    u_n = us_numb()
    print(u_n)
    check = check_numder(u_n, c_n, n)
    print(check)