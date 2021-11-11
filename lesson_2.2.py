my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

new_list = []
for i in my_list:
    if i.isdigit():
        new_list.extend(['"', f'{int(i):02}', '"'])
    elif (i.startswith('+') or i.startswith('-')) and i[1:].isdigit():
        new_list.extend(['"', f'{i[0]}{int(i[1:]):02}', '"'])
    else:
        new_list.append(i)
conclusion = ' '.join(new_list)
print(conclusion)
