import numpy as np

# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

# def bubble_sort(spisok):
#     print(spisok)
#     swapped = False
#     for i in range(len(spisok) - 1, 0, -1):
#         for j in range(i):
#             if spisok[j] < spisok[j + 1]:
#                 spisok[j], spisok[j + 1] = spisok[j + 1], spisok[j]
#                 swapped = True
#         if swapped:
#             swapped = False
#         else:
#             break
#     return spisok


# if __name__ == '__main__':
#     s = np.random.randint(-100, 101, 200)
#     print(*bubble_sort(s))

# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
array = [16.5,17.32,1.00,27.93,15.21]
print(array)
def merge_sort(nums):
  if len(nums) > 1:
    mid = len(nums) // 2
    left = nums[mid:]
    right = nums[:mid]
    merge_sort(left)
    merge_sort(right)
    i = j = k = 0
    while i < len(left) and j < len(right): 
      if left[i] < right[j]: 
          nums[k] = left[i] 
          i+=1
      else: 
          nums[k] = right[j] 
          j+=1
      k+=1
    while i < len(left): 
      nums[k] = left[i] 
      i+=1
      k+=1
    while j < len(right): 
      nums[k] = right[j] 
      j+=1
      k+=1
merge_sort(array)
print(array)
# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

# def median_search(lst):
#   if len(lst) % 2 == 0:
#     lst.append(0) # на случай, если кол-во чисел меньше медианы и больше её будет не одинаковое
#   for i in range(len(lst)):
#     max_cnt = 0
#     min_cnt = 0
#     for j in lst:
#       if lst[i] > j:
#         max_cnt += 1
#       elif lst[i] < j:
#         min_cnt += 1
#     if max_cnt == min_cnt:     
#       print(f'Медиана: {lst[i]}')

# natural_int = np.random.randint(0, 100)
# size = 2 * natural_int + 1
# array = list(np.random.choice(size, size, replace=False))
# print(f'Исходный массив: {array}')
# median_search(array)