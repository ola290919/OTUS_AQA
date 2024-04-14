"""
Программа формирования json файла заданного формата
из двух файлов books.csv и users.json
"""

import json
from csv import DictReader
from hw4 import CSV_FILE_PATH
from hw4 import JSON_FILE_PATH

def gen_result():
    """
    функция возврата нужного файла
    """
    with open(CSV_FILE_PATH, "r", newline='') as f:
        reader = DictReader(f)
        books_list = []
        for books in reader:
            books_list.append(books)

    with open(JSON_FILE_PATH, "r") as f:
        users = json.load(f)
        users_list = []
        for user in users:
            users_dict = {}
            users_dict['name'] = user['name']
            users_dict['gender'] = user['gender']
            users_dict['address'] = user['address']
            users_dict['age'] = user['age']
            users_dict['books'] = []
            users_list.append(users_dict)

    while books_list:
        for users_dict in users_list:
            if books_list:
                users_dict["books"].append(books_list.pop())
            else:
                break
    with open("result.json", "w") as f:
        json.dump(users_list, f, indent=4)


gen_result()
