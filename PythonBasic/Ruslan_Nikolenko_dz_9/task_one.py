import time

class TrafficLight:
    __color = [('красный', 7), ('желтый', 2), ('зеленый', 3)]
    def running(self):
        for c, t in self.__color:
            print(f'{c}... включен на {t} секунд...')
            time.sleep(t)

a = TrafficLight()
TrafficLight.running(a)