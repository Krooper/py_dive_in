import os

"""
Ищем все файлы в текущей директории с определенным расширением
"""
def file_finder(extension: str) -> list[str]:
    return [_ for _ in os.listdir(os.getcwd()) if _.endswith(fr"{extension}")]


"""
Выделяем у найденных файлов только имена без расширения
"""
def get_names_without_extension(files: list[str]) -> list[str]:
    return [files[i].split(".")[0] for i in range(len(files))]


"""
Выделяем этот желаемый диапазон
"""
def get_names_to_save(names_to_save: list[str], diapazon: list) -> list[str]:
    return [names_to_save[i][diapazon[0]:diapazon[1]+1] for i in range(len(names_to_save))]


"""
Создаем список из номеров, входящих в будущие имена файлов (не придумал, как сделать с помощью list comprehension)
"""
def get_counter_numbers(file_number: int, count_nums: int) -> list[str]:
    str_lst = [f'{i + 1}' for i in range(file_number)]
    for i in range(len(str_lst)):
        while len(str_lst[i]) < count_nums:
            str_lst[i] = '0' + str_lst[i]
    return str_lst


"""
Получаем список с новыми именами
"""
def get_new_names(old_name_parts: list[str], new_wanted_name: str, new_file_numbers: list[str], new_extension: str):
    return [f"{old_name_parts[i]}{new_wanted_name}{new_file_numbers[i]}{new_extension}" for i in
            range(len(old_name_parts))]


"""
Основная функция (сделал так, тчо аргумент wanted_name должен быть всегда)
"""
def rename(wanted_name: str, count_nums: int, extension_old: str, extension_new: str, diapazon: list) -> None:
    files_to_rename = file_finder(extension_old)
    if len(files_to_rename) == 0:
        print("Файлы с указанным расширением не найдены!")
        exit()

    # Сделал отдельными переменными просто для удобства чтения кода, так-то можно все в одну строчку запихнуть :)
    file_names_without_ext = get_names_without_extension(files_to_rename)  # Имена файлов без расширения
    names_to_save = get_names_to_save(file_names_without_ext, diapazon)  # Части имен, которые надо сохранить
    counter_numbers = get_counter_numbers(len(files_to_rename), count_nums)  # Порядковые номера с нужным кол-вом цифр
    new_names_lst = get_new_names(names_to_save, wanted_name, counter_numbers, extension_new)  # Новые имена

    # Переименование файлов
    for i in range(len(files_to_rename)):
        try:
            os.rename(files_to_rename[i], new_names_lst[i])
        except FileExistsError as e:
            print(e)
            exit()

    # Проверка, что файлы переименовались
    operation_lst = [f'{files_to_rename[i]} -> {new_names_lst[i]}' for i in range(len(files_to_rename))]
    print('Готово! История переименований:')
    for operation in operation_lst:
        print(f"{operation}")


if __name__ == '__main__':
    rename(wanted_name="video", count_nums=3, extension_old=".txt", extension_new=".csv", diapazon=[3, 6])
