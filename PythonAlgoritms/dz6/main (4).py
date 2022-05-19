import sys

# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

def replacement_value(arr):
  print(f'Начальный массив: {arr}')
  max_v = max(arr)
  min_v = min(arr)
  print(sys.getsizeof(max_v))
  max_index = arr.index(max_v)
  min_index = arr.index(min_v)
  arr[max_index] = min_v
  arr[min_index] = max_v
  print(sys.getsizeof(arr))
  print(f'После изменения: {arr}')
  return arr
arr = [1, 2, 3, 4, 5, 12313, 123]
replacement_value(arr)
# такие переменные как max_v/min_v, max_index/min_index имеют пространственную сложность O(1)
# переменная arr имеет сложность O(n), так вес растёт пропорционально входящим данным

def max_minimal(arr):
  max_min = min(arr)
  print(sys.getsizeof(max_min))
  if max_min >= 0:
    return 'В массиве нет отрицательных чисел'
  else: 
    return f'Максимальное отрицательное значение: {max_min} '\
           f'Позиция в массиве: {arr.index(max_min)}'

arr = [1, 2, 3, 4, -1, -2, -0.5]
print(max_minimal(arr)) 
# переменная max_min также имеет пространственную сложность O(1)
# в то время, как переменная arr будет иметь сложность O(n)