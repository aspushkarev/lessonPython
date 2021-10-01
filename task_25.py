# Реализация структуры «Рейтинг», представляющая собой набор натуральных чисел, которые не возрастают

my_list = [7, 5, 3, 3, 2]
answer = 'да'
while answer != 'нет':
    number = int(input("Введите новый элемент рейтинга: "))
    for i in range(len(my_list)):
        if number == my_list[i]:
            my_list.insert(i, number)
            print(my_list)
            break
        else:
            if number > my_list[i]:
                my_list.insert(i, number)
                print(my_list)
                break
    answer = input("Продолжаем? Введите да/нет: ")
