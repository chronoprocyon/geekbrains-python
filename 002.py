seconds = int(input("Введите время в секундах >>> "))

hours = seconds // 360

minutes = (seconds % 360) // 60

new_seconds = (seconds % 360) % 60

print(f"{hours}:{minutes}:{new_seconds}")
