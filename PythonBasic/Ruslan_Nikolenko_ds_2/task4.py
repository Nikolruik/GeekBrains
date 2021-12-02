list_unitpeople = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in range(len(list_unitpeople)):
    time_list = list_unitpeople[i].split(" ")
    unit_people = ' '.join(time_list[:-1])
    last_elem = len(time_list) - 1
    name = time_list[last_elem]
    print(f"{unit_people.capitalize()}, {name.title()}")
