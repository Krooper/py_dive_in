import random
import string

# Задание 1
def add_nums_to_file(line_num: int, file: str) -> None:
    with open(file, 'a') as f:
        for i in range(line_num):
            num1 = random.randint(-1000, 1000)
            num2 = round(random.uniform(-1000, 1000), 2)
            f.write(f"\n{num1}|{num2}")


# Задание 2
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


# Задание 3
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
        multed_nums.append(round(int(line_nums[0])*float(line_nums[1]), 2))
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


if __name__ == '__main__':
    add_nums_to_file(1, "nums.txt")
    names_generator(3)
    mult_save("nums.txt", "names.txt")
