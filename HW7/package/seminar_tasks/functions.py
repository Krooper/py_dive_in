import random
import string
import os
import shutil
from package.seminar_tasks.constraints import *

__all__ = ['add_nums_to_file', 'names_generator',
           'mult_save', 'extension_creator',
           'many_extensions_creator', 'in_folder_creator',
           'files_sorter']


"""
Задание 1
"""
def add_nums_to_file(line_num: int, file: str) -> None:
    with open(file, 'a') as f:
        for i in range(line_num):
            num1 = random.randint(-1000, 1000)
            num2 = round(random.uniform(-1000, 1000), 2)
            f.write(f"{num1}|{num2}\n")


"""
Задание 2
"""
# Генерация 1 имени
def name_generator(name_length: int) -> str:
    name = ''
    for i in range(name_length):
        name += random.choice(string.ascii_letters)
    if not name_check(name):
        return name_generator(name_length)
    return name.capitalize()

# Проверка на наличие хотя бы 1 гласной
def name_check(name: str) -> bool:
    vowels = set("aeiou")
    for letter in name:
        if letter in vowels:
            return True
    return False

# Генерация имен
def names_generator(number_of_names: int) -> None:
    names = []
    for number in range(number_of_names):
        name_len = random.randint(4, 7)
        names.append(name_generator(name_len))
    save_names_to_file(names)

# Сохранение в файл
def save_names_to_file(names: list[str]) -> None:
    with open('names.txt', 'w') as f:
        for name in names:
            f.write(f'{name}\n')


"""
Задание 3
"""
# Читаем первый файл
def nums_file_reader(nums_file: str) -> list[str]:
    with open(nums_file) as f:
        return [line for line in f]

# Читаем второй файл
def names_file_reader(names_file: str) -> list[str]:
    with open(names_file) as f:
        return [line.rstrip() for line in f]

# Перемножаем числа, полученные из первого файла
def nums_mult(nums: list[str]) -> list[float]:
    multed_nums = []
    for line in nums:
        line_nums = line.split('|')
        multed_nums.append(round(int(line_nums[0]) * float(line_nums[1]), 2))
    return multed_nums

# Смотрим на знак произведения:
def mult_pos(mult: float) -> bool:
    if mult > 0:
        return True
    return False

# Смотрим на длину списков (файлов):
def num_list_longer(nums_lst: list, names_lst: list) -> bool:
    if len(nums_lst) > len(names_lst):
        return True
    return False

# Выравнивание длины списков
def make_lists_equal(nums_lst: list, names_lst: list) -> tuple[list, list]:
    if num_list_longer(nums_lst, names_lst):
        return make_equal(nums_lst, names_lst)
    return make_equal(names_lst, nums_lst)

def make_equal(lst1: list, lst2: list) -> tuple[list, list]:
    i = 0
    while len(lst1) != len(lst2):
        lst2.append(lst2[i])
        i += 1
        if i == len(lst2):
            i = 0
    return lst1, lst2

# Генерация новых строк для записи в файл
def lines_to_write(nums: list[float], names: list[str]) -> list[str]:
    lines = []
    for i in range(len(nums)):
        if mult_pos(nums[i]):
            lines.append(f'{names[i].upper()} {round(nums[i])}')
        else:
            lines.append(f'{names[i].lower()} {abs(nums[i])}')
    return lines

# Основная функция
def mult_save(nums_file: str, names_file: str) -> None:
    nums = nums_mult(nums_file_reader(nums_file))
    names = names_file_reader(names_file)
    make_lists_equal(nums, names)
    lines_for_saving = lines_to_write(nums, names)
    with open('names_and_nums.txt', 'w') as f:
        for line in lines_for_saving:
            f.write(f'{line}\n')


"""
Задание 4
"""
# Создание имени файла случайной длины из диапазона
def generate_name_with_lenghts(min_length: int, max_name_len: int) -> str:
    name = ''
    name_length = random.randint(min_length, max_name_len)
    for i in range(name_length):
        name += random.choice(string.ascii_letters)
    return name

# Проверка, что файла с таким именем не существует
def file_exists(file: str) -> bool:
    return os.path.exists(file)

# Генерация байтов для записи в файл
def get_bytes_to_write(min_byte: int, max_byte: int) -> bytes:
    bytes_size = random.randint(min_byte, max_byte)
    return os.urandom(bytes_size)

# Основная функция
def extension_creator(extension: str, min_name_len=6, max_name_len=30, min_byte=256, max_byte=4096,
                      files_num=42) -> None:
    for i in range(files_num):
        name = generate_name_with_lenghts(min_name_len, max_name_len)
        while file_exists(f'{name}.{extension}'):
            name = generate_name_with_lenghts(min_name_len, max_name_len)
        with open(f'{name}.{extension}', 'w+b') as f:
            f.write(get_bytes_to_write(min_byte, max_byte))


"""
Задание 5
"""
# Получение списков расширений и кол-ва файлов
def get_ext_and_nums_lists(args) -> tuple[list[int], list[str]]:
    file_nums = []
    extensions = []
    for arg in args:
        if type(arg) == str:
            extensions.append(arg)
        elif type(arg) == int:
            file_nums.append(arg)
        else:
            print("Функция принимает только строки (расширения файлов) и целые числа (кол-во файлов)!")
            exit()
    # Использую способ выравнивания длины списка из 3-го задания:
    # Если один из списков длиннее, то второй заполняется до этой длины дубликатами своих же элементов начиная с 1
    make_lists_equal(file_nums, extensions)
    return file_nums, extensions

# Словарь с разрешением фалов и кол-вом файлов, которое нужно создать
def get_ext_and_nums_dict(file_nums: list[int], extensions: list[str]) -> dict[str:int]:
    ext_and_num = {}
    for i in range(len(file_nums)):
        if extensions[i] not in ext_and_num.keys():
            ext_and_num[extensions[i]] = file_nums[i]
        else:
            ext_and_num[extensions[i]] += file_nums[i]
    return ext_and_num

# Основная функция
def many_extensions_creator(*args) -> None:
    file_nums, extensions = get_ext_and_nums_lists(args)

    ext_and_num = get_ext_and_nums_dict(file_nums, extensions)

    for ext, number in ext_and_num.items():
        extension_creator(extension=ext, files_num=number)


"""
Задание 6
Проверка на совпадение имени уже есть в функции file_exists - имя будет генерироваться до того момента,
пока оно не будет уникальным
"""
# Проверка директории (директория будет создаваться только внутри той, в которой уже находимся)
def dir_creator(path: str) -> None:
    if os.path.exists(path) and os.path.isfile(path):
        print("Надо ввести название директории, а не файла!")
        exit()
    elif not os.path.exists(path):
        os.mkdir(path)
        os.chdir(path)
    else:
        os.chdir(path)

# Основная функция
def in_folder_creator(*args, path='') -> str:
    if path != '':
        path = f"{os.getcwd()}{path}"
        dir_creator(path)
    many_extensions_creator(*args)
    return path


"""
Задание 7
"""
# Получение списка файлов в папке по указанному пути
def get_files(path: str) -> list[str]:
    file_lst = []
    with os.scandir(path) as files:
        for file in files:
            file_lst.append(file.name)
    return file_lst

# Получение расширений файлов
def get_file_ext(file: str) -> str:
    return file.split('.')[1].lower()

# Перемещение одного файла
def mv_file(old_path: str, folder_name: str, file: str):
    dir_creator(folder_name)
    shutil.move(f'{old_path}/{file}', f'{os.getcwd()}/{file}')
    os.chdir(old_path)

# Основная функция
def files_sorter(path: str) -> None:
    files = get_files(path)
    for file in files:
        if os.path.isfile(file):
            if get_file_ext(file) in TEXT_EXTENSIONS:
                mv_file(path, 'texts', file)
            elif get_file_ext(file) in IMAGE_EXTENSIONS:
                mv_file(path, 'images', file)
            elif get_file_ext(file) in VIDEO_EXTENSIONS:
                mv_file(path, 'videos', file)


if __name__ == '__main__':
    add_nums_to_file(1, "nums.txt")
    names_generator(3)
    mult_save("nums.txt", "names.txt")
    extension_creator('txt', files_num=1)
    many_extensions_creator('txt', 'csv', 'doc', 1, 2, 3)
    my_path = in_folder_creator('txt', 'jpeg', 'avi', 'doc', 1, 2, 3, 4, path='/new_path')
    files_sorter(my_path)
