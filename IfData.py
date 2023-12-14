while True:
    day = int(input("Введите день Вашего рождения: "))
    month = int(input("Введите месяц Вашего рождения: "))
    year = int(input("Введите год Вашего рождения: "))

    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12: days = list(range(0,32))
        case 3 | 6 | 7 | 9 | 11: days = list(range(0,31))
        case 2: days = list(range(0,28))
        case _:
            print('Введите дату корректно!')
            continue

    iter_days = iter(days)
    for i in range (len(days)):
        next_day = next(iter_days)
        if next_day == day:
            print(str(day) + "." + str(month) + "." + str(year))









print(date)
