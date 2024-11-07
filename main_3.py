def divide(a, b):
    if b == 0:  # Проверяем, что b не равно нулю
        raise ValueError("Деление на ноль недопустимо")
    return a / b