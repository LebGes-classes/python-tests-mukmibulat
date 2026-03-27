def is_types_correct(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('Оба аргумента должны являться int или float')

def add(a, b):
    is_types_correct(a, b)

    return a + b

def subtract(a, b):
    is_types_correct(a, b)

    return a - b

def multiply(a, b):
    is_types_correct(a, b)

    return a * b

def divide(a, b):
    is_types_correct(a, b)

    if b == 0:
        raise ZeroDivisionError('Нельзя делить на 0')

    return a / b