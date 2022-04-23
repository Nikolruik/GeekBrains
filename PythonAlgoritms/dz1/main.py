import random
# task 1:
# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# def task_one(number):
#   if number.isnumeric():
#     number = int(number)
    # if number < 1000 and number >99:
    #   a = [int(i) for i in str(number)] 
    #   res1 = int(a[0]) + int(a[1]) + int(a[2])
    #   res2 = int(a[0]) * int(a[1]) * int(a[2])
    #   return f'Сумма: {res1}, Произведение: {res2}'
#   else:
#     raise f'Введённое значение не является 3-хзначным или числом'
    

# print(task_one(input()))

# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.
# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.
# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ./

# def isfloat(value):
#   try:
#     float(value)
#     return True
#   except:
#     return False

# def randomize(a, b):
#   if a.isdigit() and b.isdigit:
#     a, b = int(a), int(b)
#     result = random.randint(a, b)
#     return f'Случайное целое число: {result}'
#   elif isfloat(a) and isfloat(b):
#     a, b = float(a), float(b)
#     result = random.uniform(a, b)
#     return f'Случайное число с плавающей точкой: {result}'
#   elif any(map(str.isdigit, a)) == False and any(map(str.isdigit, b)) == False and len(a) == 1 and len(b) == 1:
#     a, b = ord(a), ord(b)
#     result = chr(random.randint(a, b))
#     return f'Случайный символ: {result}'
#   else:
#     return 'Введённое значение больше одного символа, либо не является только числом или только символом'
# print(randomize(input(), input()))

# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

# def find_num_letter(lang, symbol1, symbol2):
#   if lang == 'en':
#     number1 = ord(symbol1) - 96
#     number2 = ord(symbol2) - 96
#     res = number2 - number1 - 1
#     return f'{symbol1} - {number1} в алфавит, '\
#     f'{symbol2} - {number2} в алфавите, ' \
#     f'{res} букв между введёнными.'
#   elif lang == 'ru':
#     number1 = ord(symbol1) - 1071
#     number2 = ord(symbol2) - 1071
#     res = number2 - number1 - 1
#     return f'{symbol1} - {number1} в алфавит, '\
#     f'{symbol2} - {number2} в алфавите, ' \
#     f'{res} букв между введёнными.'

# print(
#   find_num_letter(input('en/ru: '), input('Символ 1: '), input('Символ 2: '))
# )

# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.
# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

# def leap_year(year):
#   year = int(year)
#   if year%4 == 0:
#     return f'Год высокосный'
#   else:
#     return f'Год не высокосный'
# print(leap_year(input('Введите год: ')))

# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).