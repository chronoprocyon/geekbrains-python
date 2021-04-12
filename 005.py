income = int(input("Введите выручку >>> "))
cost = int(input("Введите издержки >>> "))

if income > cost:
    print("Прибыль")
    rent = (income - cost) / income
    print("Рентабельность фирмы: ",  rent)
    emp_count = int(input("Введите количество сотрудников >>> "))
    print("Прибыль в расчтёте на одного сотрудника: ", (income - cost) / emp_count)
else:
    print("Убыток")
