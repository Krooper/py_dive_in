import re
from os import path
import itertools
"""
1) Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

"""
# Затычка для ввода
def path_input(file_path='default') -> str:
    if file_path == 'default':
        file_path = "C:\\Program Files (x86)\\Microsoft Office\\Office15\\POWERPNT.EXE"
    else:
        file_path = input("Введите полный путь до файла: ")
    return file_path


# Проверка, что это путь с пом-ю регулярного выражения
def path_check(file_path: str) -> str:
    file_path = path_input(file_path)

    reg_file_expr = r'(?:[a-zA-Z]\:|\\\\[\w\.]+\\[\w]+)\\(?:[\w\s\(\)]+\\)+([\wА-Яа-я\.\s]+)'
    if re.match(reg_file_expr, file_path) is None:
        print('Неверный путь. Повторите попытку.')
        return path_check(path_input())

    return file_path


# Разделение пути к файлу на части
def file_path_tuple(file_path: str) -> tuple[str, str, str]:
    path_to_read = path_check(file_path)
    path_to_file = path.dirname(rf'{path_to_read}')  # Путь до директории файла
    file_name = path.basename(rf'{path_to_read}')  # Имя и расширение
    file_and_ext = path.splitext(file_name)  # Делеление имени и расширения на части
    file = file_and_ext[0]  # Имя
    ext = file_and_ext[1]  # Расширение
    return path_to_file, file, ext


"""
2) Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
имена str, ставка int, премия str с указанием процентов вида «10.25%». 
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. 
Сумма рассчитывается как ставка умноженная на процент премии
"""
# Не придумал ничего лучше, кроме как использовать длину одного из списков
def dict_gen(names: list[str], rates: list[int], percents: list[str]) -> dict[str: float]:
    if len(names) != len(rates) or len(names) != len(percents):
        print("Длины входных списков не равны!")
        return None
    # Сам однострочный генератор
    return {names[i]: rates[i] * int(percents[i].split('%')[0]) / 100 for i in range(len(rates))}


"""
3) Создайте функцию генератор чисел Фибоначчи (см. Википедию)
"""
def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    """
    Первое задание
    """
    print(f"Первое задание: \n{file_path_tuple('default')}\n")


    """
    Второе задание
    """
    print("Второе задание:")
    mydict = dict_gen(["Михаил", "Иван"], [50000, 45000], ["80%", "95%"])
    for name, salary in mydict.items():
        print(f"{name}: {salary}")


    """
    Третье задание
    """
    print("\nТретье задание:")
    fibonacci = itertools.islice(fib(), 100)
    print(next(fibonacci))
    print(next(fibonacci))
    print(next(fibonacci))
    print(next(fibonacci))
    print(next(fibonacci))
