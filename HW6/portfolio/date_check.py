import time
import sys


# Коротенькая проверка даты на соответствие
def date_checker(date_to_check: str) -> bool:
    try:
        time.strptime(date_to_check, '%d.%m.%Y')
    except ValueError:
        return False
    return True


"""
Варианты ввода (передача строки в функцию/использование аргумента из консоли/ручной ввод)
Вариант с передачей аргумента из терминала сработает только если нет передаваемой строки при вызове функции
"""
def date_input(date_to_check=None) -> bool:
    if len(sys.argv) == 1 and date_to_check is None:
        return date_checker(input("Input a date: "))
    elif date_to_check is not None:
        return date_checker(date_to_check)
    else:
        return date_checker(sys.argv[1])


if __name__ == "__main__":
    print(date_input('01.21.2015'))
