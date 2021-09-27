# Программа подсчета суммы чисел n + nn + nnn

number = input("Введите любое число: ")
number1 = number + number  # складываем строки
number2 = number1 + number  # складываем строки
score = int(number) + int(number1) + int(number2)  # Подсчитываем сумму преобразуя строки в числа
print(f"Сумма чисел {number} + {number1} + {number2} = {score}")
