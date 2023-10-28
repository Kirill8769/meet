def get_list_films(list_films: list, genre: str) -> list:
    """
    Функция получает на вход список словарей,
    содержащих информацию о фильмах (например, название, жанр, режиссер и т.д.),
    и возвращает новый список, содержащий только те фильмы,
    которые относятся к заданному жанру.

    :param list_films: список словарей, содержащих информацию о фильмах
    :param genre: Жанр
    :return: Возвращает новый список,
    содержащий только те фильмы, которые относятся к заданному жанру.
    """
    result = [film for film in list_films if film["genre"] == genre.title()]
    return result


print(
    get_list_films(
        list_films=[
            {"title": "The Shawshank Redemption", "genre": "Drama", "director": "Frank Darabont"},
            {"title": "The Godfather", "genre": "Crime", "director": "Francis Ford Coppola"},
            {"title": "The Dark Knight", "genre": "Action", "director": "Christopher Nolan"},
        ],
        genre="drama",
    )
)
