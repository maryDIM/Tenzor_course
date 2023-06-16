# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_integer_number():
    assert all_division(1, 1) == 1


@pytest.mark.skip('Большие числа не проверяем')
def test_big_number():
    assert all_division(12345625, 0.12345625) == 100000000


@pytest.mark.smoke
def test_division_by_negative_number():
    assert all_division(0.2, -1) == -0.2


@pytest.mark.smoke
def test_many_numbers():
    assert all_division(64, 8, 4, 2, 1) == 1


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        assert all_division(1, 0)
