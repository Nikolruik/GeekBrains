import re

result = {}

def em_parse(mail):
    check = re.search(r'.*\@*\..{2,3}', mail)
    if check == None:
        raise ValueError(mail)
    else:
        regex = re.split(r'@', mail)
        result['username'] = regex[0]
        result['domain'] = regex[1]
    print(result)

em_parse('nikolrusik@gmail.ru')