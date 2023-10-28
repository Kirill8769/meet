def get_double_int(list_1: list, list_2: list) -> list:
    """
    Функция получает на вход два списка чисел и возвращает новый список,
    содержащий только те числа, которые встречаются в обоих списках.

    :param list_1: Список чисел
    :param list_2: Список чисел
    :return: Список чисел которые встречаются в обоих списках
    """
    result = set(list_1) & set(list_2)
    return list(result)


print(get_double_int([1, 2, 3, 4], [3, 4, 5, 6]))
