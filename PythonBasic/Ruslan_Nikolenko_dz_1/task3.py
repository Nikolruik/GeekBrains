count = 0
while True:
    if count < 100:
        count += 1
        a = str(count)
        if a[-1] == '1' and (count < 11 or count > 19):
            print(count, 'процент')
        elif a[-1] != '1' and (count < 11 or count > 19) and int(a[-1]) < 5 and a[-1] != '0':
            print(count, 'процента')
        elif a[-1] != '1' and (int(a[-1]) >= 5 or int(a[-1]) == 0 or (count > 11 or count < 19)):
            print(count, 'процентов')
    else:
        break

