i = 1
one_list = []
two_list = []
while True:
    if i >= 1000:
        i = i - 2
        break
    cube = i ** 3
    i += 2
    # print("Кубы: ", cube) ## Выводим все кубы
    sum = 0
    count = 0
    while (cube != 0):
        count += 1
        sum = sum + cube % 10
        cube = cube // 10
    sum_bonus = sum + (17 * count)
    if (sum % 7) == 0:
        one_list.append(sum)
        # print("Сумма чисел, которая делится нацело на 7: ", sum)
    elif (sum_bonus % 7) == 0:
        two_list.append(sum_bonus)
        # print("Сумма чисел +17, которая делится нацело на 7:", sum_bonus)
print(one_list)
print(two_list)