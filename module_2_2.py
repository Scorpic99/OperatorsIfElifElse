first_str = int(input('Введите первое значние: '))
second_str = int(input('Введите второе значние: '))
third_str = int(input('Введите третье значние: '))

if first_str == second_str == third_str:
    print(3)
elif first_str == second_str or second_str == third_str or first_str == third_str:
    print(2)
else:
    print(0)


