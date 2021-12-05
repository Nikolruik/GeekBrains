rus_numbers = ["Ноль", "Один", "Два", "Три", "Четыре", "Пять", "Шесть", "Семь", "Восемь", "Девять", "Десять"]
ang_numbers = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
tx = input("Число на английском: ")

def num_translate_adv(num):
    if num.capitalize() in ang_numbers:
        index_num = ang_numbers.index(num.capitalize())
        if num[0].isupper():
            print(rus_numbers[index_num].capitalize())
        else:
            print(rus_numbers[index_num].lower())
    else:
        print("Ошибка, такого числа нет в базе")
num_translate_adv(tx)