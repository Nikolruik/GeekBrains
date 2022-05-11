# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# def replacement_value(arr):
#   print(f'Начальный массив: {arr}')
#   max_v = max(arr)
#   min_v = min(arr)
#   max_index = arr.index(max_v)
#   min_index = arr.index(min_v)
#   arr[max_index] = min_v
#   arr[min_index] = max_v
#   print(f'После изменения: {arr}')
    # return arr
# arr = [1, 2, 3, 4]
# replacement_value(arr)
  
# 4. Определить, какое число в массиве встречается чаще всего.
# def max_repeat(arr):
#   return max(set(arr), key = arr.count)
  
# arr = [2, 1, 2, 2, 1, 3]
# print(max_repeat(arr))

# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

def max_minimal(arr):
  max_min = min(arr)
  if max_min >= 0:
    return 'В массиве нет отрицательных чисел'
  else: 
    return f'Максимальное отрицательное значение: {max_min} '\
           f'Позиция в массиве: {arr.index(max_min)}'

arr = [1, 2, 3, 4, -1, -2, -0.5]
print(max_minimal(arr))