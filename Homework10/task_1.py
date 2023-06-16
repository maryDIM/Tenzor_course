# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random


def generate_random_name():
    while True:
        yield ''.join([chr(random.randrange(97, 123)) for i in range(random.randint(1, 15))]) + ' ' + ''.join(
            [chr(random.randrange(97, 123)) for i in range(random.randint(1, 15))])


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
