import json
from src.archive_classes.base_archive_class import BaseArchive
from src.vacancy_classes.vacancy_class import Vacancy


class JSONArchive(BaseArchive):
    """Класс для работы с файлами формата JSON, хранящими данные о вакансиях"""

    def __init__(self, file_name: str) -> None:
        """Инициализатор класса"""
        if not file_name.endswith('.json'):
            raise ValueError('Файл должен быть формата JSON')
        self._file_name = file_name
        super().__init__()

    def write_to_file(self, raw_vacancies_list: list[dict]):
        """Добавдяет список вакансий в JSON файл"""

        with open(self._file_name, "w") as f:
            json_str = json.dumps(raw_vacancies_list, indent=2, ensure_ascii=False)
            f.write(json_str)

    def load_from_file(self):
        """Получает данные из файла и преобразовывает их в словарь вакансий"""

        with open(self._file_name, "r") as f:
            json_string = f.read()

        raw_vacancies = json.loads(json_string)
        return Vacancy.cast_to_object_list(raw_vacancies)

    def delete_from_file(self):
        """Удаляет информацию о вакансиях"""

        with open(self._file_name, "w") as f:
            f.write('')
