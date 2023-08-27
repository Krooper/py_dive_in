import os
from pathlib import Path


def folder_size(path: str) -> int:
    f_size = 0
    for file in Path(path).rglob('*'):
        if os.path.isfile(file):
            f_size += os.path.getsize(file)
    return f_size


def dir_recur(cur: str, files_inside: dict) -> dict:
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


if __name__ == '__main__':
    files_dict = {}
    files = dir_recur(r'C:\Users\Андрей\Desktop\Hogwarts Saves\cracked', files_dict)
    for key, value in files.items():
        print(f'\n{key}')
        for thing, ext in value.items():
            print(f"{thing}: {ext}")
