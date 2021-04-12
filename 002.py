seconds = int(input("Введите время в секундах >>> "))

hours = seconds // 3600

minutes = (seconds % 3600) // 60

new_seconds = (seconds % 3600) % 60

print(f"{hours}:{minutes}:{new_seconds}")
