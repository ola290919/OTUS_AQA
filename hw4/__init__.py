"""
Генерируем ссылки на файлы csv и json
"""

import os.path

FILES_DIR = os.path.dirname(__file__) # получаем полный путь к папке, в которой находится текущий файл


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename) # присоединяем к пути до папки название файла и получаем путь до конкретного файла


CSV_FILE_PATH = get_path(filename="books.csv")
JSON_FILE_PATH = get_path(filename="users.json")
