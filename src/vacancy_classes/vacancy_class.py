class Vacancy:
    """класс для работы с вакансией"""
    def __init__(self, title: str, url: str, salary: int, requirements: str | None,
                 responsibility: str | None, area: str | None) -> None:
        """Инициализатор класса"""
        self._title = title
        self._url = url
        self._salary = salary
        self._requirements = requirements
        self._responsibility = responsibility
        self._area = area

    @property
    def title(self) -> str:
        """Возвращает название вакансии"""
        return self._title

    @property
    def url(self) -> str:
        """Возвращает ссылку на вакансию"""
        return self._url

    @property
    def salary(self) -> int:
        """Возвращает данные о зарплате"""
        return self._salary

    @property
    def requirements(self) -> str | None:
        """Возвращает требования из вакансии"""
        return self._requirements

    @property
    def responsibility(self) -> str | None:
        """Возвращает данные о зарплате"""
        return self._responsibility

    @property
    def location(self) -> str | None:
        """Возвращает локацию вакансии"""
        return self._location
