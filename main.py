from src.config import EMPLOYERS_ID
from src.DBManager import DBManager
from src.employers import Employers
from src.vacancies import Vacancies
from src.utils import add_database


def main():
    """Основной интерфейс программы."""

    print(f"\nВ программе есть информация по открытым вакансиям следующих работодателей: ")
    [print(employer['name']) for employer in EMPLOYERS_ID]

    add_database()
    hhru_employers = Employers()
    hhru_employers.add_data_to_database()
    hhru_vacancies = Vacancies()
    hhru_vacancies.add_data_to_database()
    db_manager = DBManager()

    # do_it = True
    #
    # while do_it:
    #
    #     choice = int(input('h;k;'))
    #
    #     if choice == 0:
    #         print('Спасибо, что попробовали данную программу. До свидания!')
    #         do_it = False
    #
    #     elif choice == 1:
    #         print("Наименование работодателя | Кол-во открытых вакансий")
    #         print("__________________________|_________________________")
    #         [print(f"{employer[0] + ((26 - len(employer[0])) * ' ')}| {employer[1]}") for employer in
    #          db_manager.get_companies_and_vacancies_count()]
    #         print("\n")
    #
    #     elif choice == 2:
    #         print(f'{db_manager.get_all_vacancies()}\n')
    #
    #     elif choice == 3:
    #         print(f'Средняя зарплата = {db_manager.get_avg_salary()}\n')
    #
    #     elif choice == 4:
    #         print(f'{db_manager.get_vacancies_with_higher_salary()}\n')
    #
    #     elif choice == 5:
    #         keyword = input('Наберите слово для поиска в названии вакансий: \n')
    #         print(f'{db_manager.get_vacancies_with_keyword(keyword)}\n')
    #
    #     else:
    #         print('Введено не допустимое значение, пожалуйста, повторите')


if __name__ == '__main__':
    main()