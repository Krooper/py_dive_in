import os
from pathlib import Path

import json
import csv
import pickle


class Folder:
    def __init__(self, path_to_folder: str):
        self.path_to_folder = path_to_folder
        self.files_inside = {}
        self.files_inside = self.get_files_inside(self.path_to_folder, self.files_inside)

    def get_files_inside(self, folder: str, files: dict) -> dict[str: dict]:
        for smth in os.listdir(folder):
            abs_path = os.path.join(folder, smth)
            if os.path.isdir(abs_path):
                size = self.folder_size(abs_path)
                files[abs_path] = {"name": f"{smth}",
                                   "parent": folder.split('\\')[-1],
                                   "type": "dir",
                                   "size": size}
                files.update(self.get_files_inside(abs_path, files))
            elif os.path.isfile(abs_path):
                files[abs_path] = {"name": f"{smth}",
                                   "parent": folder.split('\\')[-1],
                                   "type": "file",
                                   "size": os.path.getsize(os.path.join(folder, smth))}
        return files

    @staticmethod
    def folder_size(path: str) -> int:
        f_size = 0
        for file in Path(path).rglob('*'):
            if os.path.isfile(file):
                f_size += os.path.getsize(file)
        return f_size

    def json_save(self) -> None:
        json_data = json.dumps(self.files_inside, indent='\t')
        with open('data.json', 'w') as json_file:
            json_file.write(json_data)

    def csv_save(self) -> None:
        with open('data.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(('path', 'name', 'parent', 'type', 'size'))
            for file, prop in self.files_inside.items():
                writer.writerow((file, prop['name'], prop['parent'], prop['type'], prop['size']))

    def pickle_save(self) -> None:
        with open('data.dat', 'wb') as pickle_file:
            pickle.dump(self.files_inside, pickle_file)

    def __str__(self):
        out_str = ''
        for folder, file in self.files_inside.items():
            out_str += f'\n{folder}:\n\t'
            for attribute, value in file.items():
                out_str += f'{attribute}: {value}; '
        return out_str


if __name__ == '__main__':
    my_folder = Folder(r'D:\test')

    my_folder.json_save()
    my_folder.csv_save()
    my_folder.pickle_save()

    print(my_folder)
