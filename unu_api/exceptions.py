"""
Исключения
"""


class ApiError(Exception):
    """
    Родительский класс для исключений
    """


class AuthError(ApiError):
    """
    Исключение при отсутствие токена
    """

    def __str__(self):
        return "Укажите значение переменной API_KEY"


class BalanceError(ApiError):
    """
    Исключения при отрицательном балансе
    """

    def __str__(self):
        return "На вашем балансе отсутствуют средства"


class RequestError(ApiError):
    """
    Исключение для неуспешных запросов к API
    """

    def __str__(self):
        return "Запрос к API выполнен с ошибкой"


class JsonParsingError(ApiError):
    """
    Исключение для ошибок декодирования Json
    """

    def __str__(self):
        return "Не удалось декодировать JSON (возможно данный метод API сломан)"


class UnknowError(ApiError):
    """
    Для неизвестных ошибок
    """

    def __str__(self):
        return "Неизвестная ошибка"
