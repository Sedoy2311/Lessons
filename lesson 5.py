"""Задание №1"""
def odd_nums(number: int) -> int:
    """Генератор, возвращающий по очереди нечетные целые числа от 1 до number (включительно)"""
    for i in range(1, n + 1, 2):
        yield i

n = 15
generator = odd_nums(n)
for _ in range(1, n + 1, 2):
    print(next(generator))
# next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration

"""Задание №3"""
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Ибрагим', 'Мистер Твистер', 'Алёша']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def check_gen(tutors: list, klasses: list):

    gen = ((tutors[i], klasses[i]) if len(klasses) > i else (tutors[i], None) for i in range(len(tutors)))
    return gen

generator = check_gen(tutors, klasses)
print(type(generator))
for _ in range(len(tutors)):
    print(next(generator))
# next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration

"""Задание №4"""
def get_numbers(src: list):
    add = [b for a, b in zip(src, src[1:]) if a < b]
    return add

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(*get_numbers(src))

"""Задание №5"""
def get_uniq_numbers(src: list):
    unique_brands = set()
    tmp = set()
    for el in src:
        if el not in tmp:
            unique_brands.add(el)
        else:
            unique_brands.discard(el)
        tmp.add(el)
    unique_brands_ord = [el for el in src if el in unique_brands]
    return unique_brands_ord

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))