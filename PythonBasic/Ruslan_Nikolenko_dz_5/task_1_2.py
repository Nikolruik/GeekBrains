import sys
# task 1
def nums_generator(max_num):
    for num in range(1, max_num + 1, 2):
        yield num  # or

nums_gen = nums_generator(100)

print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))

# task 2
# def nums_generator(max_num):
#     for num in range(1, max_num + 1, 2):
#         print(num)
#
# nums_gen = nums_generator(100)