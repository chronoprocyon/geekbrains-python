first_day = int(input("Введите км за первый день >>> "))
goal = int(input("Введите цель км >>> "))

day_number = 1

while first_day < goal:
    first_day = first_day * 1.1
    day_number = day_number + 1

print(day_number)