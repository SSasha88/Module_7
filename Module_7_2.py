print('Задача "Записать и запомнить"')
print()
def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, mode='w', encoding='utf-8')
    for i, string in enumerate(strings, start=1):
        position = file.tell()
        file.write(string + '\n')
        strings_positions[(i, position)] = string
    file.close()
    return strings_positions

#Пример результата выполнения программы
#Пример выполняемого кода

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)