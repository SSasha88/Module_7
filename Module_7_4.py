print('Задание "Форматирование строк"')

# Использование %  "%s" для строк, "%d" для целых чисел и "%x" для шестнадцатеричных чисел
# Переменная для количества участников первой команды
print("Использование %")
team1_num = int(input('Введите количество участников первой команды: '))    #5
# Форматирование строки с одной переменной
string_with_team1_num = "В команде Мастера кода участников: %d" % team1_num
print(string_with_team1_num)
# Переменные для количества участников в обеих командах
team2_num = int(input('Введите количество участников второй команды: '))   #6
# Форматирование строки с двумя переменными
string_with_both_teams = "Итого сегодня в командах участников: %d и %d" % (team1_num, team2_num)
print(string_with_both_teams)
print()

# Использование format()
print('Использование format()')
# Переменная для количества задач, решённых командой 2
a = int(input('Введите количество задач, решённых командой 2 '))  #42
score_2 = a
# Форматирование строки с одной переменной
string_with_score_2 = "Команда Волшебники данных решила задач: {}".format(score_2)
print(string_with_score_2)
# Переменная для времени, за которое команда 2 решила задачи
team2_time = 18015.2
# Форматирование строки с одной переменной
string_with_team2_time = "Волшебники данных решили задачи за {} с ".format(team2_time)
print(string_with_team2_time)
print()

# Использование f-строк
print('Использование f-строк')
# Переменные для количества решённых задач по командам
score_1 = 40
score_2 = a
# Форматирование строки с двумя переменными
string_with_scores = f"Команды решили {score_1} и {score_2} задач."
print(string_with_scores)

if score_1 > score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = "Победа команды Мастера кода!"
elif score_1 < score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = "Победа команды Волшебники данных!"
else:
    challenge_result = "Ничья!"


# Форматирование строки с одной переменной
string_with_challenge_result = f"Результат битвы: {challenge_result}"
print(string_with_challenge_result)

# Переменные для общего количества задач и среднего времени решения
tasks_total = score_1 + score_2
time_avg = 45.2

# Форматирование строки с двумя переменными
string_with_tasks_and_time = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!"
print(string_with_tasks_and_time)


