import sys

def show_sale(argv):
    with open('files/bakery.csv', 'r', encoding='UTF-8') as bakery:
        if len(argv) == 1:
            print(f'Все записи:\n'
                  f'--------------------------------')
            for line in bakery:
                print(line.strip())
            print(f'--------------------------------')

        elif len(argv) == 2:
            print(f'Все записи с {argv[1]}:\n'
                  f'--------------------------------')
            for linenum, line in enumerate(bakery):
                if linenum >= int(argv[1]):
                    print(line.strip())
            print(f'--------------------------------')
        elif len(argv) > 2:
            print(f'Записи с {argv[1]} по {argv[2]}:\n'
                  f'--------------------------------')
            for linenum, line in enumerate(bakery):
                if linenum >= int(argv[1]) and linenum < int(argv[2]):
                    print(line.strip())
            print(f'--------------------------------')
        else:
            print('Слишком много аргументов')

if __name__ == '__main__':
    exit(show_sale(sys.argv))