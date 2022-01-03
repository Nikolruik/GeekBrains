def type_logger(func):
    def txt(num):
        res = func(num)
        print(f'{func.__name__} ({num}: {type(num)})')
    return txt

@type_logger
def calc_cube(x):
    return x ** 3
calc_cube(5)