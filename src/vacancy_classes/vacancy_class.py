class Vacancy:
    """класс для работы с вакансией"""
    def __init__(self, name: str, url: str, salary: str, salary_min: int, salary_max: int,
                 requirements: str | None, responsibility: str | None, area: str | None) -> None:
        """Инициализатор класса"""
        self._name = name
        self._url = url
        self._salary = salary
        self._salary_min = salary_min
        self._salary_max = salary_max
        self._requirements = requirements
        self._responsibility = responsibility
        self._area = area

    @property
    def name(self) -> str:
        """Возвращает название вакансии"""
        return self._name

    @property
    def url(self) -> str:
        """Возвращает ссылку на вакансию"""
        return self._url

    @property
    def salary(self) -> str:
        """Возвращает данные о зарплате"""
        return self._salary

    @property
    def salary_min(self) -> int:
        """Возвращает данные о минимальной зарплате"""
        return self._salary_min

    @property
    def salary_max(self) -> int:
        """Возвращает данные о максимальной зарплате"""
        return self._salary_max

    @property
    def requirements(self) -> str | None:
        """Возвращает требования из вакансии"""
        return self._requirements

    @property
    def responsibility(self) -> str | None:
        """Возвращает данные о зарплате"""
        return self._responsibility

    @property
    def area(self) -> str | None:
        """Возвращает локацию вакансии"""
        return self._area

    @classmethod
    def cast_to_object_list(cls, raw_vacancies):
        """Преобразование набора данных в список объектов"""

        vacancies_list = []
        for rv in raw_vacancies:
            attributes = [rv.get('name'),
                          rv.get('url'),
                          f'{rv.get("salary", {}).get("from")} - {rv.get("salary", {}).get("to")}',
                          rv.get('snippet', {}).get('requirement'),
                          rv.get('snippet', {}).get('responsibility'),
                          rv.get('area', {}).get('name')]
            vacancy = Vacancy(*attributes)
            vacancies_list.append(vacancy)
