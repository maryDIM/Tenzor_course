# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.


class TestNewTask:

    def test_1(self, info_start_time_class, info_time_test):
        print('Тест 1')

    def test_2(self, info_end_time_class):
        print('Тест 2')