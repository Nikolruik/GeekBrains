import cProfile

# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

# homework 2, dz 3:
def mirroring(a):
    num = str(a)
    reverse_num = []
    for i in num:
        if i.isdigit:
            reverse_num.insert(0, i)
    return print(''.join(reverse_num))

# cProfile.run('mirroring(1)')
# 7 function calls in 0.000 seconds
# cProfile.run('mirroring(12)')
# 8 function calls in 0.000 seconds
# cProfile.run('mirroring(123)')
# 9 function calls in 0.000 seconds
# cProfile.run('mirroring(1234)')
# 10 function calls in 0.001 seconds

# Сложность алгоритма - O(n), поскольку количество вызовов растёт с количеством входных данных
