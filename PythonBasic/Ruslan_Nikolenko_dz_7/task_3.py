# TASK 3
import os

project = 'my_project'
struct = os.walk(project)
def f_in_template:
    for f in struct:
        name_fold = f[0].split('\\')
        for temp_f in f[2]:
            if '.html' in temp_f:
                way_dir = os.path.join(r'my_project/templates/', name_fold[-1])
                with open(f'{f[0]}\\{temp_f}', 'r', encoding='UTF-8') as temporary:
                    content = temporary.read()
                    if not os.path.exists(way_dir):
                        if not os.path.exists(r'my_project/templates/'):
                            os.mkdir(r'my_project/templates/')
                        os.mkdir(way_dir)
                    with open(f'my_project\\templates\\{name_fold[-1]}\\{temp_f}', 'w', encoding='UTF-8') as result_f:
                        result_f.write(content)
    print('Шаблоны перенесены')