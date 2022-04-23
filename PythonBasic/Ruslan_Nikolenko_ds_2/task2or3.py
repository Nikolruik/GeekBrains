start_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
len_list = len(start_list)

for i in range(len_list):
    item = start_list.pop(0)
    if item.isdigit() and item.isalnum():
        start_list.append('"')
        start_list.append(f'{int(item):02d}')
        start_list.append('"')
    elif item[0] == "+" and item[1].isdigit():
        start_list.append('"')
        start_list.append(f'+{int(item):02d}')
        start_list.append('"')
    else:
        start_list.append(item)

print(' '.join(start_list))