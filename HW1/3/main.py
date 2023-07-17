# 3. Напишите код, который запрашивает число и сообщает, является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.


def int_check(number):
    try:
        return int(number)
    except ValueError:
        print("Вы ввели не число! Повторите ввод!")
        return int_check(input())


def range_check(number):
    number = int_check(number)
    if 0 <= number <= 10**5:
        return number
    else:
        print("Число за пределами диапазона! Повторите ввод!")
        return range_check(input())


def prime_num_check(number):
    k = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            k = k + 1
    if k <= 0:
        return "Число простое."
    else:
        return "Число не является простым."


if __name__ == '__main__':
    num = input("Введите число от 0 до 100000: ")
    print(prime_num_check(range_check(num)))
