# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
# Пример:
# Ввод:
# 1/2
# 1/3
# Вывод:
# 5/6 1/6
import re, fractions


# Поиск общего делителя
def common(m,n):
    while m%n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m%old_n
    return n


# Из списка дробей (список из строк) делаем словарь, в качестве значений которого
# выступают списки числителя и знаменателя дроби, ключи - номер дроби.
# *(так-то словарь тут особо не нужен, но посчитал, что было удобно итерироваться в случае кол-ва дробей больше, чем 2)
def frac_segmenter(frac_lst: list[str]) -> dict[int:[int]]:
    segments_out = {}
    for i in range(len(frac_lst)):
        segments = frac_lst[i].split("/")
        segments_i = []
        for segment in segments:
            segments_i.append(int(segment))
        segments_out[i + 1] = segments_i
    return segments_out


# Проверка дроби на соответствие формату:
# 1) числитель и знаменатель проверяются на то, что в них ненулевое целое положительно число
# 2) сама дробь проверяется на то, что в ней есть слеш
def frac_pattern_check(frac_to_check: str,
                       pattern='(^[1-9]\d*)|(^([1-9][0-9]*){1,3})|(^\+?[1-9][0-9]*)') -> bool:
    try:
        frac_lst = frac_to_check.split("/")
        for num in frac_lst:
            if re.fullmatch(rf'{pattern}', num) is None:
                return False
        return True
    except ValueError:
        return False


# Ввод дробей, выдает список из них
def frac_input(frac_number=2) -> list[str]:
    frac_out_lst = []
    for i in range(frac_number):
        frac = input(f"Введите {i + 1}-ю дробь в формате 'Х/Х' (Х - ненулевое положительно число): ")
        while not frac_pattern_check(frac):
            frac = input(f"Ошибка ввода!\nВведите {i + 1}-ю дробь в формате 'Х/Х' (Х - ненулевое положительно число): ")
        frac_out_lst.append(frac)
    return frac_out_lst


# Класс с магическими методами
class MyFraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        numerator = self.numerator * other.denominator + self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        com = common(numerator, denominator)
        return MyFraction(numerator//com, denominator//com)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        com = common(numerator, denominator)
        return MyFraction(numerator//com, denominator//com)


# Тут есть "магические числа" в качестве индексов списков
# Возникают, потому что не хотел писать программу для совсем уж общего случая (при кол-ве дробей больше, чем 2)
# При этом все методы имеют соответствующий параметр (кол-во дробей) там, где это необходимо.
if __name__ == '__main__':
    fractions_dict = frac_segmenter(frac_input())

    fractions_lst = []
    std_fractions_list = []
    for fraction in fractions_dict.values():
        new_frac = MyFraction(fraction[0], fraction[1])
        std_frac = fractions.Fraction(fraction[0], fraction[1])
        fractions_lst.append(new_frac)
        std_fractions_list.append(std_frac)

    print(f"Сумма: {fractions_lst[0] + fractions_lst[1]}")
    print(f"Произведение: {fractions_lst[0] * fractions_lst[1]}")

    print("\nПроверочные значения:")
    print(f"Сумма: {std_fractions_list[0] + std_fractions_list[1]}")
    print(f"Произведение: {std_fractions_list[0] * std_fractions_list[1]}")
