# """Задание №1"""
# def num_translate(value: str) -> str:
# #     """переводит числительное с английского на русский """
#     my_dict = {
# 'one': 'один',
# 'two': 'два',
# 'three': 'три',
# 'four': 'четыре',
# 'five': 'пять',
# 'six': 'шесть',
# 'seven': 'семь',
# 'eight': 'восемь',
# 'nine': 'девять',
# 'ten': 'десять'}
#
#     str_out = my_dict.get(value)
#     return str_out
#
# print(num_translate('one'))
# print(num_translate('eight'))
#
# """Задание №3"""
# def thesaurus(*args) -> dict:
#     dict_out = {}  # результирующий словарь значений
#
#     for name in args:
#         key = name[0].capitalize()
#         if key not in dict_out:
#             dict_out[key] = []
#         dict_out[key].append(name)
#
#     return dict_out
#
# print(thesaurus("Иван", "Мария", "Петр", "Илья"))
#
# """Задание №5"""
# from random import choice
#
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# list_1 = []
#
# def get_jokes(n, flag=False):
#     for i in range(n):
#         random_index = choice(nouns)
#         random_index_1 = choice(adverbs)
#         random_index_2 = choice(adjectives)
#         joke = f'{random_index} {random_index_1} {random_index_2}'
#         list_2 = []
#         print(joke)
#         if flag == True:
#             list_2 = joke.split()
#             for noun in nouns:
#                 for fun in list_2:
#                     if noun == fun:
#                         nouns.remove(noun)
#
#             for adverb in adverbs:
#                 for fun in list_2:
#                     if adverb == fun:
#                         adverbs.remove(adverb)
#
#             for adjective in adjectives:
#                 for fun in list_2:
#                     if adjective == fun:
#                         adjectives.remove(adjective)
#
# print(get_jokes(n=2, flag=True))
# print(get_jokes(n=10, flag=True))