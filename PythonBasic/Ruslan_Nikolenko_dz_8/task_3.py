def type_logger(func):
    def txt(*a):
        check = a
        for item in check:
            print(f'{item}: {type(item)}', end=',')
        return a
    return txt

@type_logger
def calc_cube(*args):
    return args

print(calc_cube(5, 6))