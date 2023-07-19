# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
# Пример:
# Ввод:
# 1/2
# 1/3
# Вывод:
# 5/6 1/6
import re, fractions


def frac_segmenter(frac_lst: list[str]) -> dict[int:int]:
    segments_out = {}
    for i in range(len(frac_lst)):
        segments = frac_lst[i].split("/")
        segments_i = []
        for segment in segments:
            segments_i.append(int(segment))
        segments_out[i + 1] = segments_i
    return segments_out


def frac_pattern_check(frac_to_check: str,
                       pattern='(?:\d{1,2}(?:\.\d+)?|100(?:\.0+)?)/(?:\d{1,2}(?:\.\d+)?|100(?:\.0+)?)') -> bool:
    if re.fullmatch(rf'{pattern}', frac_to_check) is None:
        return False
    return True


def frac_input(frac_number=2) -> list[str]:
    frac_out_lst = []
    for i in range(frac_number):
        frac = input(f"Введите {i + 1}ю дробь в формате Х/Х (Х не больше 100): ")
        while not frac_pattern_check(frac):
            frac = input(f"Ошибка ввода!\nВведите {i + 1}-ю дробь в формате Х/Х (Х не больше 100): ")
        frac_out_lst.append(frac)
    return frac_out_lst


class MyFraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        numerator = self.numerator * other.denominator + self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return MyFraction(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return MyFraction(numerator, denominator)


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
