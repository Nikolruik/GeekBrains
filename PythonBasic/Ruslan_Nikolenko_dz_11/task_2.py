class MyError(Exception):
    def __init__(self):
        pass

try:
    a = input('Введите число: ')
    if int(a) == 0:
        raise MyError()
    else:
        print(100 / int(a))
except ValueError:
    print('Вы ввели не число')
except MyError:
    print('На 0 делить нельзя')