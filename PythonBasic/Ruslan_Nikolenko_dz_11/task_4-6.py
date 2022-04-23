class Warehouses:
    def __init__(self):
        pass
#####################################################
class Office_equip:
    units = []
    techs = {}
    techs_u = {}

    def __init__(self):
       pass

    def add_unit(self, unit):
        self.units.append(unit)

    def show_all(self):
        print(f'Инфо о технике: {self.techs} \n'
              f'Все отделы: {self.units} \n'
              f'Техника по отделам: {self.techs_u}')

#####################################################
class Printer(Office_equip):
    def __init__(self, type, size, color):
        super().__init__()
        self.name = 'printer'
        self.type = type
        self.size = size
        self.color = color

    def add_tech(self, count):
        if self.name not in super().techs:
            super().techs[self.name] = [{'Количество': count}, {'Размер': self.size}, {'Цвет': self.color},
                                        {'Тип':self.type}]

    def moving(self, w, count): #wf - откуда, w - куда, count - сколько
        if w in super().units:
            if super().techs[self.name] != None:
                super().techs_u[w] = {self.name: super().techs[self.name]}
                for k, v in {self.name: super().techs[self.name][0]}.items():
                    for k2, v2 in v.items():
                        v[k2] = count
            else:
                print('Такой техники не существует')
        else:
            print('Такого отдела не существует')
###########################################################
class Scanner(Office_equip):
    def __init__(self, speed, size, color):
        super().__init__()
        self.name = 'scanner'
        self.speed = speed
        self.size = size
        self.color = color

    def add_tech(self, count):
        if self.name not in super().techs:
            super().techs[self.name] = [{'Количество': count}, {'Размер': self.size}, {'Цвет': self.color},
                                        {'Скорость печати':self.speed}]
    def moving(self, w, count): #wf - откуда, w - куда, count - сколько
        if w in super().units:
            if super().techs[self.name] != None:
                super().techs_u[w] = {self.name: super().techs[self.name]}
                for k, v in {self.name: super().techs[self.name][0]}.items():
                    for k2, v2 in v.items():
                        v[k2] = count
            else:
                print('Такой техники не существует')
        else:
            print('Такого отдела не существует')

#####################################################
class Xerox(Office_equip):
    def __init__(self, print_cl, size, color):
        self.name = 'xerox'
        self.print_cl = print_cl
        self.size = size
        self.color = color

    def add_tech(self, count):
        if self.name not in super().techs:
            super().techs[self.name] = [{'Количество': count}, {'Размер':self.size}, {'Цвет':self.color},
                                        {'Цвет печати':self.print_cl}]
        else:
            print('Техника уже имеется')

    def moving(self, w, count): #wf - откуда, w - куда, count - сколько
        if str(count).isdigit():
            pass
        else:
            raise ValueError('Количество не может быть строкой')
        if w in super().units:
            if super().techs[self.name] != None:
                super().techs_u[w] = {self.name: super().techs[self.name]}
                for k, v in {self.name: super().techs[self.name][0]}.items():
                    for k2, v2 in v.items():
                        v[k2] = count
            else:
                print('Такой техники не существует')
        else:
            print('Такого отдела не существует')



a = Xerox('red', '122x500', 'white')
b = Printer('струйный', '122x32', 'red')
a.add_tech(1)
b.add_tech(2)
a.show_all()
a.add_unit('Офис')
a.moving('Офис', 2)
a.show_all()
