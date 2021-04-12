months = int(input("Сколько месяцев в году? >>>"))

days = int(input("Сколько дней в году? >>> "))

days_per_month = days // months

first_month = input("Первый месяц в году? >>> ")

last_month = input("Последний месяц в году? >>> ")

print("В году", months, "месяцев", days, "дней.", "В месяце в среднем", days_per_month, "дней.", first_month, "- первый месяц в году. Последний месяц -", last_month)
