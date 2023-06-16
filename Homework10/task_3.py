# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('prepare_data', [pytest.param((1, 1, 1), marks=pytest.mark.smoke),
                                          (12345625, 0.12345625, 100000000),
                                          (0.2, -1, -0.2),
                                          (64, 8, 4, 2, 1, 1),
                                          pytest.param((1, 0, 0), marks=pytest.mark.skip('Деление на ноль. Скип'))
                                          ],
                         ids=['positive', 'big numbers', 'division by negative number', 'many numbers',
                              'division by zero'])

def test_all_division(prepare_data):
    assert all_division(*prepare_data[:-1]) == float(prepare_data[-1])
