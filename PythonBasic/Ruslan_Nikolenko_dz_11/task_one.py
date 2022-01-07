import datetime

class Data:
    # def __init__(self, date):

    @classmethod
    def classmethod(cls, date):
        list = date.split('-')
        for i in list:
            list.remove(i)
            list.append(int(i))
        print(list)
        return cls

    @staticmethod
    def staticmethod(dates):
        now = datetime.datetime.now()
        list = dates.split('-')
        if int(list[0]) > 31 or int(list[0]) <= 0:
            print('День указан неверно')
        elif int(list[1]) > 12 or int(list[1]) <= 0:
            print('Месяц указан неверно')
        elif int(list[2]) > now.year or int(list[2]) <= 0:
            print('Год указан неверно')
        else:
            print('Дата введена корректно')


a = Data()
Data.staticmethod('32-12-2021')
print(a.classmethod('21-12-2021'))
print(Data.staticmethod('32-12-2021'))
