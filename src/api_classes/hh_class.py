import json

import requests
from src.api_classes.parser_class import Parser


class HeadHunterAPI(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        self._url = 'https://api.hh.ru/vacancies'
        self._headers = {'User-Agent': 'HH-User-Agent'}
        self._params = {'text': '', 'page': 0, 'per_page': 100}
        self._vacancies = []
        super().__init__()

    def get_vacancies_by_keyword(self, keyword: str) -> list:
        """Функция для подключения к API и получения ответа от get-запроса.
        Запись ответа в список вакансий в формате JSON"""

        self._params['text'] = keyword
        while self._params.get('page') != 20:
            response = requests.get(self._url, headers=self._headers, params=self._params)
            vacancies = response.json().get('items', [])
            self._vacancies.extend(vacancies)
            self._params['page'] += 1
        self.write_to_file()

        return self._vacancies

    def write_to_file(self):
        with open("data/vacancies.json", "w") as f:
            json_str = json.dumps(self._vacancies, indent=2, ensure_ascii=False)
            f.write(json_str)
