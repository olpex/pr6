# Це бібліотека/модуль з функціями
def greet_user(name):
    return f"Привіт, {name}! Ласкаво просимо до нашої програми."

def calculate_square(number):
    """Функція для обчислення квадрату числа"""
    return number ** 2

def check_even_odd(number):
    """Функція для перевірки чи є число парним або непарним"""
    if number % 2 == 0:
        return f"Число {number} є парним"
    else:
        return f"Число {number} є непарним"
