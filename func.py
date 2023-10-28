def get_int_list(int_list: list) -> list:
    """
    Функция получает на вход список чисел
    и возвращает новый список, содержащий только числа,
    которые меньше среднего значения списка

    :param int_list: Список целых чисел
    :return: Отсортированный список целых чисел
    """
    result = [i for i in int_list if i < sum(int_list) / len(int_list)]
    return result


print(get_int_list([1, 2, 3, 4, 5]))
