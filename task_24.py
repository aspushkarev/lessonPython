# Пользователь вводит строку. Программа выводит каждое слово с новой строки

words = input("Введите строу из нескольких слов: ")
# print(words.split())
word = words.split()

for i in range(len(word)):  # проходим циклом для печати
    if len(word[i]) <= 10:  # проверяем, если слово до 10 символов, то печать
        print(i + 1, ')', word[i])
    else:
        short_word = word[i]
        print(i + 1, ')', short_word[:10])  # иначе обрезаем остальные символы превышающие 10
