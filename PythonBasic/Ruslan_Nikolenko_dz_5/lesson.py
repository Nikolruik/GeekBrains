import sys
# nums = []
# for num in range(1, 10 ** 4 + 1, 2)
#     nums.append(num ** 2)
#
# print(type(nums), sys.getsizeof(nums), nums)

# nums_gen = (num ** 2 for num in range(1, 10**2 + 1, 2)) #создание генератора
# print(type(nums_gen), sys.getsizeof(nums_gen), nums_gen) #
# print(type([1, 9]), sys.getsizeof([1, 9]), [1, 9])
#
# print(list(nums_gen))
# print('Цикл')
# for i in nums_gen:
#     print(i)
#
# print('list')
# print(list(nums_gen))
#
# def nums_generator(max_num):
#     for num in range(1, max_num + 1, 2):
#         yield num ** 2
#
# nums_gen = nums_generator(10 ** 6)
# print(type(nums_gen), sys.getsizeof(nums_gen), nums_gen)
# print(sum(nums_gen))

#Compressions start

# nums_cube_gen = (sum ** 3 for num in range(5 + 1))
# nums_cube = list(nums_cube_gen)
# print(tyoe(nums_cube_gen), *nums_cube_gen)
#
nums_cube = [num for num in range(5 + 1) ]
print(type(nums_cube), nums_cube)

# weather_data = [
#     [-17.5, -18.9, -21.0, -16.1],
#     [-9.3, -11.7, -14.3, -15.8],
#
# ]