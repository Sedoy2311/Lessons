# Задание №1
def convert_time(duration: int) -> str:

    day = duration // (24 * 3600)
    sec = duration % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60
    if day > 0:
        i = "{} дн {} ч {} мин {} сек".format(day, hour, min, sec)
    elif hour > 0:
        i = "{} ч {} мин {} сек".format(hour, min, sec)
    elif min > 0:
        i = "{} мин {} сек".format(min, sec)
    else:
        i = "{} сек".format(sec)
    return i

duration = -123456
if duration < 0:
    print('Число не должно быть отрицательным')
else:
    result = convert_time(duration)
    print(result)

# # Задание №2
# def sum_list_1(dataset: list) -> int:
#     list_1 = []
#     for i in range(1, 1001, 2):
#         list_1.append(i ** 3)
#     numbers_sum = 0
#     for i in list_1:
#         n = 0
#         j = i
#         while i > 0:
#             n += i % 10
#             i //= 10
#         if n % 7 == 0:
#             numbers_sum += j
#
#     return numbers_sum
#
# def sum_list_2(dataset: list) -> int:
#     list_2 = []
#     for i in range(1, 1001, 2):
#         list_2.append(i ** 3 + 17)
#     numbers_sum = 0
#     for i in list_2:
#         n = 0
#         j = i
#         while i > 0:
#             n += i % 10
#             i //= 10
#         if n % 7 == 0:
#             numbers_sum += j
#
#     return numbers_sum
#
# my_list = []
# result_1 = sum_list_1(my_list)
# print(result_1)
# result_2 = sum_list_2(my_list)
# print(result_2)
#
# # Задание №3
# def transform_string(number: int) -> str:
#
#     i = n % 10
#     if 11 <= n <= 19:
#         text = f'{n} процентов'
#     elif i == 1:
#         text = f'{n} процент'
#     elif 2 <= i <= 4:
#         text = f'{n} процента'
#     else:
#         text = f'{n} процентов'
#     return text
#
#
# for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
#     print(transform_string(n))