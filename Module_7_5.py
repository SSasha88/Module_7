import os
import time

# Директория для обхода
directory = r"C:\Users\User\PycharmProjects\Module_7"
# Дерево каталогов
for root, dirs, files in os.walk(directory):
    # Перебираю все файлы в текущей директории
    for file in files:
        # Полный путь к файлу
        filepath = os.path.join(root, file)
        # Время последнего изменения файла
        filetime = os.path.getmtime(filepath)
        # Преобразую время в форматированный вид
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        # Размер файла
        filesize = os.path.getsize(filepath)
        # Родительская директория файла
        parent_dir = os.path.dirname(filepath)
        # Вывод информации о файле
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')