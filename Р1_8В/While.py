from numb_comp import cnumb
from check import check_number

def whl():

    c_numb = cnumb()
    while True:

        u_numb = int(input('Введите Ваше число '))
        print(u_numb)
        answer = check_number(u_numb, c_numb)
        print(answer)
        if u_numb == c_numb:
            break

whl()


