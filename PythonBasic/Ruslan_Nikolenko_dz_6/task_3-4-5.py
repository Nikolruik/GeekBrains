# task 3
# with open('users.csv', 'r', encoding='UTF-8') as users,  open('hobby.csv', 'r', encoding='UTF-8') as hobbys:
#     dicte = {}
#     for hobby, user in zip(hobbys, users):
#         cl_hobby = hobby.replace('\n', '')
#         cl_user = user.replace('\n', '')
#         dicte[cl_user] = cl_hobby
#     print(dicte)


# task 4
# with open('users.csv', 'r', encoding='UTF-8') as users,  open('hobby.csv', 'r', encoding='UTF-8') as hobbys, open('result_3.csv', 'w+', encoding='UTF-8') as new_f:
#     for hobby, user in zip(hobbys, users):
#         cl_hobby = hobby.replace('\n', '')
#         cl_user = user.replace('\n', '')
#         new_f.write(f'{cl_user}:{cl_hobby}\n')
#     new_f.seek(0)
#     print(new_f.read())
#


# task 5
# def combination(users_inp, hobbys_inp, result_inp):
#         with open(f'files/{users_inp}', 'r', encoding='UTF-8') as users, open(f'files/{hobbys_inp}', 'r', encoding='UTF-8') as hobbys, open(
#                 f'files/{result_inp}', 'w+', encoding='UTF-8') as new_f:
#             for hobby, user in zip(hobbys, users):
#                 cl_hobby = hobby.replace('\n', '')
#                 cl_user = user.replace('\n', '')
#                 new_f.write(f'{cl_user}:{cl_hobby}\n')
#             new_f.seek(0)
#             print(new_f.read())
# combination(input('Введите файл имён: '), input('Введите файл интересов: '), input('Введите результирующий файл: '))