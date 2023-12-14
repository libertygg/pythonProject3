ticket_number = [int(i) for i in input('Введите номер билета (6 цифр): ')]
"""
tn_lst = list(ticket_number)

num1 = tn_lst[0]
num1_int = int(num1)
num2 = tn_lst[1]
num2_int = int(num2)
num3 = tn_lst[2]
num3_int = int(num3)
num4 = tn_lst[3]
num4_int = int(num4)
num5 = tn_lst[4]
num5_int = int(num5)
num6 = tn_lst[5]
num6_int = int(num6)

sum_first_3_nums = int(num1_int+num2_int+num3_int)
sum_second_3_nums = int(num4_int+num5_int+num6_int)

if sum_first_3_nums == sum_second_3_nums:
    print("Билет счастливый!")
else:
    print("НЕ В ЭТОТ РАЗ")
"""
if sum(ticket_number[:3]) == sum(ticket_number[3:]):
    print("Билет счастливый!")
else:
    print("НЕ В ЭТОТ РАЗ")