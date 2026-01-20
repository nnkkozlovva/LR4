# TODO импортировать необходимые молули


import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # Считываем содержимое csv файла
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as csv_file:
        # Используем DictReader для чтения CSV
        csv_reader = csv.DictReader(csv_file)

        # Преобразуем OrderedDict в обычный словарь и собираем все строки в список
        data = [dict(row) for row in csv_reader]

    # Сериализуем в JSON файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME, encoding='utf-8') as output_f:
        for line in output_f:
            print(line, end="")
