class Stationary:
    title = 'Parent'

    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Pen(Stationary):
    title = 'Pen'

    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Pencil(Stationary):
    title = 'Pencil'

    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Handler(Stationary):
    title = 'Handler'

    def draw(self):
        print(f'Запуск отрисовки {self.title}')

a, b, c, d = Stationary(), Pen(), Pencil(), Handler()

a.draw(), b.draw(), c.draw(), d.draw()