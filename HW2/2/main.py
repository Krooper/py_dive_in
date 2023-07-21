# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def int_check(number: str) -> bool:
    try:
        int(number)
        return True
    except ValueError:
        print("Вы ввели не число или число не целое! Повторите ввод!")
        return False


def positive(number: str) -> str:
    if number[0] == '-':
        return number[1:]
    return number


def dec_to_hex(decimal_number: str, base=16) -> str:
    digits = "0123456789abсdef"
    decimal_number = int(decimal_number)
    hex_number = ''
    while decimal_number > 0:
        hex_number = digits[decimal_number % base] + hex_number
        decimal_number = decimal_number // base
    return hex_number


if __name__ == '__main__':
    number = input("Введите положительное целое число: ")
    while not int_check(number):
        number = input("Введите положительное целое число: ")
    number = positive(number)

    print(f"Ваше число: {number}")
    hex_number = dec_to_hex(number)
    check_hex_number = hex(int(number))[2:]
    print(f"Ваше число в двоичной системе счисления: {hex_number}")
    print(f"Число для проверки: {check_hex_number}")
