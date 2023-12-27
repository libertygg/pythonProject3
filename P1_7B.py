from random import randint

n_comp = randint(1, 100)
print(n_comp)
print('Компьютер "загадал" число в интервале от 1 до 100. Какое?')

def att(func):
    func.data = 0
    return func

@att
def check_numder(numder, n_comp):
    check_numder.data += 1
    if numder > n_comp:
        return 'Загаданное число меньше'
    elif otvet < n_comp:
        return 'Загаданное число больше.'
    else:
        return f'Правильно! Число попыток отгадывания - {check_numder.data}'

while True:

    otvet = int(input('Введите Ваше число '))
    answer = check_numder(otvet, n_comp)
    print(answer)
    if otvet == n_comp:
        break