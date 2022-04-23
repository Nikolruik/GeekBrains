from requests import get, utils
from pyquery import PyQuery as pq
response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)

def currency_rates(charcode):
    charcode = charcode.upper()
    doc = pq(response.content)
    for i in doc:
        text = pq(i).text()
        curr = text.split("\n")
    if charcode in curr:
        i_currency = curr.index(f"{charcode}")
        i_currency_val = i_currency + 3
        i_currency_nominal  = i_currency + 1

        print(f"{curr[i_currency_nominal]} {curr[i_currency]} это {curr[i_currency_val]} руб")
    else:
        print('None')
# currency_rates(input("Введите ключ валюты(USD, AUD и др): ").upper())

if __name__ == '__main__':
    import sys