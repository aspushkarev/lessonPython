# Подсчёт количества дней для достижения цели в беге

first_day = int(input('Введите вашу дистанцию в км: '))
aim = int(input('Введите вашу цель в км: '))
i = 1
while first_day <= aim:
    first_day = first_day + (first_day * 0.1)
    i += 1  # Подсчитываем количество дней до цели
print(f"На {i} день вы достигните цели")
