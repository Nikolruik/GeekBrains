class comp:
    def __init__(self, i):
        self.i = i

    def __mul__(self, other):
        return comp(self.i * other.i)

    def __truediv__(self, other):
        return comp(self.i / other.i)
    
    def __str__(self):
        return f'{self.i}'

a = comp(complex(1, 2))
b = comp(complex(2, 4))
z = a * b
e = a / b
print(z, e)