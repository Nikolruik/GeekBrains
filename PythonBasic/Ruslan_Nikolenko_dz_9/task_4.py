class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed, self.color, self.name, self.is_police = speed, color, name, is_police

    def go(self):
        print(f'{self.color} {self.name} поехала')
    def stop(self):
        print(f'{self.color} {self.name} остановилась')
    def turn(self, direction):
        self.direction = direction
        print(f'{self.color} {self.name} повернула на {self.direction}')

    def show_speed(self):
        print(f'Скорость: {self.speed}')
    def check_police(self):
        print(f'Полицейская: {self.is_police}')

class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f'Скорость: {self.speed}') if self.speed <= 60 else print('Превышина допустимая скорость')

    def check_police(self):
        print(self.is_police)
class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
    def show_speed(self):
        print(f'Скорость: {self.speed}') if self.speed <= 40 else print('Превышина допустимая скорость')
class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)
    def check_police(self):
        print(f'Полицейская: {self.is_police}')

c, t, s, w, p = Car(40, 'White', 'Audi'), TownCar(40, 'Black', 'BMW'), SportCar(40, 'Red', 'Ferrari'),\
                WorkCar(40, 'Blue', 'BobCat'), PoliceCar(40, 'Green', 'Skoda')

t.go(), t.turn('лево'), t.stop()
t.show_speed(), t.check_police()
print(f'Марка: {c.name}, Color: {c.color}, Speed: {c.speed}, Is police: {c.is_police}')













