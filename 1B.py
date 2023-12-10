name = input('Введите имя и фамилию: ')
name_tit = name.title()
name_spl = name_tit.split(' ')
first_name = name_spl[0]
last_name = name_spl[1]
last_name_lst = list(last_name)
login = first_name + last_name_lst[0]
print(login)
