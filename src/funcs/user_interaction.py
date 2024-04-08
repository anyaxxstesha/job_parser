from src.api_classes.hh_class import HeadHunterAPI
from src.vacancy_classes.vacancy_class import Vacancy
from src.vacancy_classes.vacancy_manager import VacancyManager


# Функция для взаимодействия с пользователем
def user_interaction():
    """
    Функцию для взаимодействия с пользователем через консоль. Данная функция реализует:

    Ввод поискового запроса для запроса вакансий из hh.ru;
    Получение топ N вакансий по зарплате (N запрашивает у пользователя);
    Пллучение вакансии с ключевым словом в описании.

    """

    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ")
    salary_min, salary_max = map(int, input("Введите диапазон зарплат: ").split())  # Пример: 100000 150000

    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()

    # Получение вакансий с hh.ru по ключевому слову
    hh_vacancies = hh_api.get_vacancies_by_keyword(search_query)

    # Преобразование набора данных в список объектов
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    data = VacancyManager(vacancies_list)

    filtered_vacancies = data.filter_vacancies(vacancies_list, filter_words)
    ranged_vacancies = data.get_vacancies_by_salary(filtered_vacancies, salary_min, salary_max)
    sorted_vacancies = data.sort_vacancies(ranged_vacancies)
    top_vacancies = data.get_top_vacancies(sorted_vacancies, top_n)

    print("\n\n")
    for vacancy in top_vacancies:
        print(vacancy, end="\n\n\n")
