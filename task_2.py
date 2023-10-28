def get_str_list(str_list: list) -> list:
    """
    Функция получает на вход список строк
    и возвращает новый список, содержащий только уникальные строки

    :param str_list: список строк
    :return: уникальные строки
    """
    return sorted(set(str_list))


print(get_str_list(['apple', 'banana', 'orange', 'apple']))
