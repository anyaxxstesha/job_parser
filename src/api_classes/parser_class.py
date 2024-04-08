from abc import ABC, abstractmethod


class Parser(ABC):
    """Абстрактный класс для работы с API"""

    def __init__(self) -> None:
        """Инициализатор класса"""
        pass

    @abstractmethod
    def get_vacancies_by_keyword(self, keyword: str) -> None:
        """Функция для подключения к API и получения ответа от get-запроса.
        Запись ответа в список вакансий"""

        pass
