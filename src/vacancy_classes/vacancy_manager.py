from src.vacancy_classes.vacancy_class import Vacancy


class VacancyManager:
    """Класс для работы с вакансиями"""

    def __init__(self, vacancies: list[Vacancy]) -> None:
        """Инициализатор класс"""
        self._vacancies = vacancies

    def __len__(self) -> int:
        """Возвращает количество вакансий в списке"""
        return len(self.vacancies)

    @property
    def vacancies(self):
        """Возвращает список вакансий"""
        return self._vacancies

    @staticmethod
    def filter_vacancy_by_keywords(vacancy: Vacancy, filter_words: str) -> bool:
        """Фильтрация по ключевому слову для одной вакансии"""
        for attribute in vacancy.__dict__.values():
            if filter_words in str(attribute):
                return True
        return False

    def filter_vacancies(self, vacancies: list[Vacancy], filter_words: str) -> list[Vacancy]:
        """Фильтрация по ключевому слову для всех вакансии"""

        filtered_vacancies = list(
            filter(
                lambda vacancy: self.filter_vacancy_by_keywords(vacancy, filter_words),
                vacancies
            )
        )

        return filtered_vacancies

    @staticmethod
    def get_vacancies_by_salary(filtered_vacancies: list[Vacancy],
                                salary_min: int, salary_max: int) -> list[Vacancy]:
        """Возвращает вакансии с определенной зарплатной вилкой"""

        if salary_max < salary_min:
            raise ValueError("Максимальная зарплата не должна быть меньше минимальной")

        ranged_vacancies = list(
            filter(
                lambda vacancy: salary_min <= vacancy.salary_min and salary_max >= vacancy.salary_max,
                filtered_vacancies
            )
        )

        return ranged_vacancies

    @staticmethod
    def sort_vacancies(ranged_vacancies: list[Vacancy]) -> list[Vacancy]:
        """Возвращает отсортированные по зарплате вакансии"""

        sorted_vacancies = sorted(ranged_vacancies, key=lambda vacancy: vacancy.salary_max, reverse=True)

        return sorted_vacancies

    @staticmethod
    def get_top_vacancies(sorted_vacancies: list[Vacancy], n: int) -> list[Vacancy]:
        """Возвращает топ n вакансий"""

        top_vacancies = sorted_vacancies[0:n]
        return top_vacancies

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Добавление вакансии"""
        self.vacancies.append(vacancy)

    def del_vacancy(self, vacancy: Vacancy) -> None:
        """Удаление вакансии"""
        self.vacancies.remove(vacancy)
