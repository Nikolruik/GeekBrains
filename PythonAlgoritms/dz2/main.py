import random

# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
def counter():
    num = list(input('Введите число: '))
    even_cnt = 0
    n_even_cnt = 0
    for i in num:
        if i.isdigit:
            if int(i) % 2 == 0:
                even_cnt = even_cnt + 1
            elif int(i) % 2 != 0:
                n_even_cnt = n_even_cnt + 1
    print(f'Кол-во чётных: {even_cnt} '
          f'Кол-во нечётных: {n_even_cnt}')
counter()

# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

def mirroring():
    num = list(input('Введите число: '))
    reverse_num = []
    for i in num:
        if i.isdigit:
            reverse_num.insert(0, i)
    return print(''.join(reverse_num))
# mirroring()

# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.
def game():
    rand = random.randrange(0, 100)
    attempt = 0
    while attempt < 10:
        attempt = attempt + 1
        num = int(input('Угадай число от 0 до 100: '))
        if attempt != 10:
            if num > rand:
                print('Ваше число больше загадонного')
            elif num < rand:
                print('Ваше число меньше загаданного')
            elif num == rand:
                print(f'Вы победили, загаданное число - {rand}. Попытка: {attempt}')
                return print(rand)
        elif attempt == 10:
            return print(f'Вы проиграли, загаданное число: {rand}')
# game()

# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

def cnt_num():
    numers = input('Введите последовательность чисел через запятую:')
    find = int(input('Число, которое надо найти:'))
    numers = numers.split(',')
    repeat = 0
    for i in numers:
        if int(i) == find:
            repeat = repeat + 1
    print(f'Кол-во совпадений: {repeat}')
# cnt_num()

