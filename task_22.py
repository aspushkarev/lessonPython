# Обмен значений соседних элементов списка

list_user = list(input('Введите текст из нескольких слов: '))
j = 0
for i in range(len(list_user) // 2):
    list_user[j], list_user[j + 1] = list_user[j + 1], list_user[j]
    j += 2
print(list_user)
