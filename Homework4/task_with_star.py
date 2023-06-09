# Задача со ЗВЁЗДОЧКОЙ. Решать НЕ обязательно.
# Программа получает на вход натуральное число num.
# Программа должна вывести другое натуральное число, удовлетворяющее условиям:
# Новое число должно отличаться от данного ровно одной цифрой
# Новое число должно столько же знаков как исходное
# Новое число должно делиться на 3
# Новое число должно быть максимально возможным из всех таких чисел
# Например (Ввод --> Вывод) :
#
# 379 --> 879
# 15 --> 75
# 4974 --> 7974

def max_division_by_3(num):
    my_list = list(str(num))
    super_num = []
    for i in range(len(my_list)):
        del_elem = my_list.pop(i)  # удалим элемент
        for j in range(9, -1, -1):
            my_list.insert(i, str(j))  # на его место вставим элемент из последовательности (9, 0)
            new_num = ''.join(my_list)
            if len(new_num) == len(my_list) and (int(new_num) % 3 == 0) and (int(new_num) != num):
                new_num = int(new_num)
                super_num.append(int(new_num))
            my_list.pop(i)
        my_list.insert(i, del_elem)

    new_num = max(super_num)
    return new_num


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    379, 810, 981, 4974, 996, 9000, 15, 0, 9881, 9984, 9876543210, 98795432109879543210
]

test_data = [
    879, 870, 987, 7974, 999, 9900, 75, 9, 9981, 9987, 9879543210, 98798432109879543210
]

for i, d in enumerate(data):
    assert max_division_by_3(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
