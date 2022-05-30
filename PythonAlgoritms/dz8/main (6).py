# 1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N, состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.

import hashlib


def substring_count(input_string):
    input_string = str(input_string).lower()
    length = len(input_string)
    hash_set = set()
    for i in range(length + 1):
        for j in range(i + 1, length + 1):
            h = hashlib.sha1(input_string[i:j].encode('utf-8')).hexdigest()
            hash_set.add(h)

    return len(hash_set)


some_string = 'hello'

print(f'Количество различных подстрок в строке {some_string}: {substring_count(some_string)}')

# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.

# from collections import Counter

# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right


# def get_code(head, codes=dict(), code=''):
#     if head is None:
#         return None
#     if isinstance(head.value, str):
#         codes[head.value] = code
#         return codes
#     get_code(head.left, codes, code+'0')
#     get_code(head.right, codes, code+'1')

#     return codes


# def get_tree(stroka):
#     str_count = Counter(stroka)

#     if len(str_count) <= 1:
#         node = Node(None)

#         if len(str_count) == 1:
#             node.left = Node(str_count[0])
#             node.right = Node(None)
#         str_count : {node: 1}

#     while len(str_count) != 1:
#         node = Node(None)
#         spam = str_count.most_common()[:-3:-1]
        
#         if isinstance(spam[0][0], str):
#             node.left = Node(spam[0][0])

#         else:
#             node.left = spam[0][0]

#         if isinstance(spam[1][0], str):
#             node.right = Node(spam[1][0])

#         else:
#             node.right = spam[1][0]

#         del str_count[spam[0][0]]
#         del str_count[spam[1][0]]
#         str_count[node] = spam[0][1] + spam[1][1]

#     return [key for key in str_count][0]


# def coding(string, codes):
#     res = ''

#     for symbol in string:
#         res += codes[symbol]

#     return res


# def decoding(string, codes):
#     res = ''
#     i = 0

#     while i < len(string):

#         for code in codes:

#             if string[i:].find(codes[code]) == 0:
#                 res += code
#                 i += len(codes[code])

#     return res


# my_string = input('Введите строку для сжатия: ')
# tree = get_tree(my_string)

# codes = get_code(tree)
# print(f'Шифр: {codes}')

# coding_str = coding(my_string, codes)
# print('Сжатая строка: ', coding_str)

# decoding_str = decoding(coding_str, codes)
# print('Исходная строка: ', decoding_str)

# if my_string == decoding_str:
#     print('Успешно!')
# else:
#     print('Ошибка!')