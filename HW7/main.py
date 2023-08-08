from package import *
import os

if __name__ == '__main__':
    first_dir = os.getcwd()

    # Задачи с семинара
    add_nums_to_file(1, "nums.txt")
    names_generator(3)
    mult_save("nums.txt", "names.txt")
    extension_creator('txt', files_num=1)
    many_extensions_creator('txt', 'csv', 'doc', 1, 2, 3)
    my_path = in_folder_creator('txt', 'jpeg', 'avi', 'doc', 1, 2, 3, 4, path='/new_path')
    files_sorter(my_path)

    os.chdir(first_dir)

    # Задача по переименованию файла
    rename(wanted_name="video", count_nums=3, extension_old=".txt", extension_new=".csv", diapazon=[3, 6])