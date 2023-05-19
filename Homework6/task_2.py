# Нелокальные изменения
# Имеется функция global_function с локальной переменной msg = 1
# Ваша задача дополнить логику функции global_function следующим образом:
# global_function должна содержать в себе функцию local_function
# local_function должна изменить значение переменной msg на значение 2

def global_function():
    """
    Функция, содержащая локальную функцию.
    :return: переменная
    """
    msg = 1

    def local_function():
        """
        Функция для переопределения переменной в объемлющей области видимости.
        :return: переменная
        """
        nonlocal msg
        msg = 2

        return msg

    local_function()

    return msg


assert global_function() == 2, 'Значение переменной msg должно быть равно 2'
print('Все ок')
