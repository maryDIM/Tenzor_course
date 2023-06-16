import datetime
import pytest


@pytest.fixture
def info_time_test():
    start = datetime.datetime.now()
    yield
    end = datetime.datetime.now()
    print(f'Время выполнения теста - {end - start}')


@pytest.fixture
def info_start_time_class():
    print(f'Начало выполнения класса {datetime.datetime.now()}')


@pytest.fixture
def info_end_time_class():
    yield
    print(f'Конец выполнения класса {datetime.datetime.now()}')
