class Clothes:

    def __init__(self, v=0, h=0):
        self.v = float(v)
        self.h = float(h)

    def coat(self):
        if self.v != 0.0:
            result = self.v / 6.5 + 0.5
        else:
            result = 0
        return result

    def suit(self):
        if self.h != 0.0:
            result = 2 * self.h + 0.3
        else:
            result = 0
        return result

    def summ(self):
        result = self.coat() + self.suit()
        return result

a = Clothes(54, 175)
print(f'Расход ткани на пальто: {a.coat()}')
print(f'Расход ткани на костюм: {a.suit()}')
print(f'Расход ткани на пальто и костюм: {a.summ()}')