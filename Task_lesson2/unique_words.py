'''Контейнерные типы данных:
Задача: Написать программу, которая принимает на вход строку и
возвращает список всех уникальных слов в этой строке.
При этом использовать только базовые операции, цикл for, функции и контейнерные типы данных.

Тесты:'''




# def unique_words(lst):
#     finish_list = []
#     new_list = []
#     for i in lst.split():
#         if i in new_list:
#             continue
#         else:
#             new_list.append(i)
#     # for x in range(0, len(new_list)):
#     #     if "," in new_list[x]:
#     #         new_list.pop(-1)

    # print(new_list)
    # return new_list


def unique_words(string):
    # создаем пустой список для уникальных слов
    unique_words = []

    stop_symbols = r'.,!?;:()[]{}<>'

    # удаляем из строки все знаки препинания
    for stop_symbol in stop_symbols:
        string = string.replace(stop_symbol, '')

    # разбиваем строку на список слов
    words = string.split()

    # проходим циклом по каждому слову и добавляем его в список
    # уникальных слов, если оно еще не было добавлено
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

    return unique_words




assert unique_words("hello world") == ["hello", "world"]
assert unique_words("apple apple banana cherry") == ["apple", "banana", "cherry"]
assert unique_words("Python is great, isn't it?") == ["Python", "is", "great", "isn't", "it"]
