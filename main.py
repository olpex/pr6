from functions import greet_user, calculate_square, check_even_odd

def main():
    # Тестування функції привітання
    name = input("Введіть ваше ім'я: ")
    print(greet_user(name))
    
# Тестування функції обчислення квадрату числа
    number = int(input("Введіть число для обчислення його квадрату: "))
    print(f"Квадрат числа {number} дорівнює: {calculate_square(number)}")
    
# Тестування функції перевірки на парність/непарність
    test_number = int(input("Введіть число для перевірки на парність/непарність: "))
    print(check_even_odd(test_number))

if __name__ == "__main__":
    main() 
