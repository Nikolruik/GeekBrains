import collections


# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.


# def analytic(n):
#   l = collections.defaultdict(list)
#   all_summ = 0
#   for i in range(n):
#     name = input(f'Введите название предприятия {i + 1}: ')
#     cvartals = input('Доходы за 4 квартала: ').split(',')
#     cvartals = list(map(float, cvartals))
#     l[name].append(cvartals)
#     total = sum(l[name][0])
#     l[name].append(total)
#     all_summ += l[name][1]
#     middle = all_summ / n
#   m_avg = []
#   l_avg = []
#   for i in l:
#     if l[i][1] >= middle:
#       m_avg.append(i)
#     else:
#       l_avg.append(i)
#   print(f'Средний доход компаний за год: {middle}')
#   print(f'Компании, чей доход больше среднего: {m_avg}')
#   print(f'Компании, чей доход меньше среднего: {l_avg}')

# analytic(int(input('Введите кол-во компаний: ')))


# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# def sum_hex(x, y):
#     HEX_NUM = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
#                'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
#                0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
#                10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
#     result = collections.deque()
#     transfer = 0
#     if len(y) > len(x):
#         x, y = collections.deque(y), collections.deque(x)
#     else:
#         x, y = collections.deque(x), collections.deque(y)
#     while x:
#         if y:
#             res = HEX_NUM[x.pop()] + HEX_NUM[y.pop()] + transfer
#         else:
#             res = HEX_NUM[x.pop()] + transfer
#         transfer = 0
#         if res < 16:
#             result.appendleft(HEX_NUM[res])
#         else:
#             result.appendleft(HEX_NUM[res - 16])
#             transfer = 1
#     if transfer:
#         result.appendleft('1')
#     return list(result)
# def mult_hex(x, y):
#     HEX_NUM = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
#                'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
#                0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
#                10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
#     result = collections.deque()
#     spam = collections.deque([collections.deque() for _ in range(len(y))])
#     x, y = x.copy(), collections.deque(y)
#     for i in range(len(y)):
#         m = HEX_NUM[y.pop()]
#         for j in range(len(x) - 1, -1, -1):
#             spam[i].appendleft(m * HEX_NUM[x[j]])
#         for _ in range(i):
#             spam[i].append(0)
#     transfer = 0
#     for _ in range(len(spam[-1])):
#         res = transfer
#         for i in range(len(spam)):
#             if spam[i]:
#                 res += spam[i].pop()
#         if res < 16:
#             result.appendleft(HEX_NUM[res])
#         else:
#             result.appendleft(HEX_NUM[res % 16])
#             transfer = res // 16
#     if transfer:
#             result.appendleft(HEX_NUM[transfer])
#     return list(result)


# a = list(input('Введите 1-е шестнадцатиричное число: ').upper())
# b = list(input('Введите 2-е шестнадцатиричное число: ').upper())
# # print(a, b)

# print(*a, '+', *b, '=', *sum_hex(a, b))

# print(*a, '*', *b, '=', *mult_hex(a, b))
