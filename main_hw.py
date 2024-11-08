#  Функция для вычисления остатка от деления
def calculate_remainder(dividend, divisor):
    if divisor == 0:
        raise ValueError("Cannot divide by zero!")
    try:
        return dividend % divisor
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero!")