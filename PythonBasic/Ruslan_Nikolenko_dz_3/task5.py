from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(count):
    while True:
        if count > 0:
            one, two, three = choice(nouns), choice(adverbs), choice(adjectives)
            
            print(f'["{one} {two} {three}"]')
            count -= 1
        else:
            break
get_jokes(int(input("Введите кол-во шуток: ")))
# count_jokes = int(input("Введите кол-во шуток: "))
