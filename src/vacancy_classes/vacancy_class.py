class Vacancy:
    """класс для работы с вакансией"""
    def __init__(self, title: str, url: str, salary: int, requirements: str | None,
                 responsibility: str | None, location: str) -> None:
        """Инициализатор класса"""
        self._title = title
        self._url = url
        self._salary = salary
        self._requirements = requirements
        self._responsibility = responsibility
        self._location = location
