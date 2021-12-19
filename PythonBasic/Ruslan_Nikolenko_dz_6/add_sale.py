import sys

def add_sale(argv):
    summ = argv
    with open('files/bakery.csv', 'a', encoding='UTF-8') as bakery:
        wr = summ[-1]
        bakery.write(f'\n{str(wr)}')

if __name__ == '__main__':
    exit(add_sale(sys.argv))