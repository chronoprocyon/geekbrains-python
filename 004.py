number = int(input("Введите число >>> "))

max_number = 0

while number > 0:
    temp_number = number % 10
    if max_number < temp_number:
        max_number = temp_number
    number = number // 10
else:
    print(max_number)




