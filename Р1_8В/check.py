from dec import att

@att
def check_number(c_numb, n_comp):
    check_number.data += 1
    if c_numb > n_comp:
        return 'Загаданное число меньше'
    elif c_numb < n_comp:
        return 'Загаданное число больше.'
    else:
        return f'Правильно! Число попыток отгадывания - {check_number.data}'