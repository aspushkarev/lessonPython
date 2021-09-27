# Ввод времени в секундах, а вывод в ЧЧ:ММ:СС

seconds_input = int(input('Введите время в секундах: '))

hours = seconds_input // 3600  # находим часы
minutes_tmp = seconds_input % 3600  # находим минуты в секундах
minutes = minutes_tmp // 60  # переводим секунды в минуты
seconds = minutes_tmp % 60   # находим секунды

# Выводим найденные часы-минуты-секунды
print(f"Время в формате ЧЧ:ММ:СС:   {hours}:{minutes}:{seconds}")
