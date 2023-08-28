import os
from pathlib import Path

import json
import csv
import pickle

"""
Получаем размер папки
"""
def folder_size(path: str) -> int:
    f_size = 0
    for file in Path(path).rglob('*'):
        if os.path.isfile(file):
            f_size += os.path.getsize(file)
    return f_size


"""
Обходим всю папку
"""
def dir_recur(cur: str, files_inside: dict) -> dict[str: dict]:
    for smth in os.listdir(cur):
        abs_path = os.path.join(cur, smth)
        if os.path.isdir(abs_path):
            size = folder_size(abs_path)
            files_inside[abs_path] = {"name": f"{smth}",
                                      "parent": cur.split('\\')[-1],
                                      "type": "dir",
                                      "size": size}
            dir_recur(abs_path, files_inside)
        elif os.path.isfile(abs_path):
            files_inside[abs_path] = {"name": f"{smth}",
                                      "parent": cur.split('\\')[-1],
                                      "type": "file",
                                      "size": os.path.getsize(os.path.join(cur, smth))}
    return files_inside


"""
Запись в json
"""
def json_save(data: dict[str: dict]) -> None:
    json_data = json.dumps(data, indent='\t')
    with open('data.json', 'w') as json_file:
        json_file.write(json_data)


"""
Запись в сsv
"""
def csv_save(data: dict[str: dict]) -> None:
    with open('data.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(('path', 'name', 'parent', 'type', 'size'))
        for file, prop in data.items():
            writer.writerow((file, prop['name'], prop['parent'], prop['type'], prop['size']))


"""
Запись в pickle
"""
def pickle_save(data: dict[str: dict]) -> None:
    with open('data.dat', 'wb') as pickle_file:
        pickle.dump(data, pickle_file)


if __name__ == '__main__':
    files_dict = {}
    files = dir_recur(r'D:\WhatsAppPortable\App\AppInfo', files_dict)

    json_save(files)
    csv_save(files)
    pickle_save(files)
