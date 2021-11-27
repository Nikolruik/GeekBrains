duration = int(input("Введите секунды: "))

sec_in_min = 60
sec_in_hour = 3600
sec_in_day = 86400
sec_in_weeks = 604800

minutes = duration // sec_in_min
sec = duration - (minutes * sec_in_min)
hours = duration // sec_in_hour
days = duration // sec_in_day
weeks = duration // sec_in_weeks

if duration < sec_in_min:
    print(f"{duration} секунд")
elif duration < sec_in_hour:
    print(f"{minutes} минут {sec} секунд")
elif duration < sec_in_day:
    minutes = minutes - (hours * sec_in_min)
    print(f"{hours} час(а, ов) {minutes} минут {sec} секунд")
elif duration < sec_in_weeks:
    minutes = minutes - (hours * sec_in_min)
    hours = hours - (days * 24)
    print(f"{days} дней {hours} час(а, ов) {minutes} минут {sec} секунд")
else:
    minutes = minutes - (hours * sec_in_min)
    hours = hours - (days * 24)
    days = days - (weeks * 7)
    print(f"{weeks} недель {days} дней {hours} час(а, ов) {minutes} минут {sec} секунд")
