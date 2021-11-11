my_list = [10, 4.4, 25, 66, 88.1, 21, 77.99, 9, 666, 777.22, 999.99]
print(id(my_list))
sorted(my_list)
print(id(my_list))
for i in my_list:
    rub = int(i)
    kk = (i - rub) * 100
    print(f'{rub} рублей, {kk:02.0f} копеек', end=', ')

my_list = [10, 4.4, 25, 66, 88.1, 21, 77.99, 9, 666, 777.22, 999.99]
for i in sorted(my_list)[::-1][:5]:
    rub = int(i)
    kk = (i - rub) * 100
    print(f'{rub} рублей, {kk:02.0f} копеек')
