prices = [32.1, 44.17, 58.9, 104.55, 84.4, 20.1, 36.38, 934.6, 489.8, 1.1]
#  А разве 32.1р будет 32.01? Мне кажется, что правильнее будет 32.10. Оставьте обратную связь на счёт этого момента, пожалуйста

for price in sorted(prices):
    price_str = str(price)
    if len(price_str.split('.')[1]) < 2:
        print(" руб 0".join(price_str.split(".")), "коп", end=", ")
    else:
        print(" руб ".join(price_str.split(".")), "коп", end=", ")

print()
price_reverse = sorted(prices.copy())
price_reverse.reverse()
print(f"Сортировка по убыванию: {price_reverse}")
print(f"5 самых дорогих: {price_reverse[:6]}")
