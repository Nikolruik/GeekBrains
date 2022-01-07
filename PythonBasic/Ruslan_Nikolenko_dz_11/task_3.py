class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt
        print(self.txt)

list = []
while True:
    item = input('"stop" - чтобы остановить скрипт \n' 
                 'Введите число: ')
    try:
        if item.isdigit():
            list.append(int(item))
            print(list)
        elif item == 'stop':
            print('Работа завершена \n', list)
            break
        else:
            print(list)
            raise MyError('Введено не число')
    except MyError:
        pass

