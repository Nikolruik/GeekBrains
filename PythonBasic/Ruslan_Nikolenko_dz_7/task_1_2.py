# TASK 1
import os

dir_project = r'my_project/'
ld = ['setting', 'mainapp', 'adminapp', 'autchapp']
if not os.path.exists(dir_project):
    os.mkdir(dir_project)
    for d in ld:
        dir_patch = os.path.join(dir_project, d)
        if not os.path.exists(dir_patch):
            os.mkdir(dir_patch)

