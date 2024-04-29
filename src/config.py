from configparser import ConfigParser

URL_VACANCIES = 'https://api.hh.ru/vacancies/'
URL_EMPLOYERS = 'https://api.hh.ru/employers/'
EMPLOYERS_ID = [
    {'id': 3399, 'name': 'Deutsche Bank'},
    {'id': 6093775, 'name': 'Aston'},
    {'id': 1189354, 'name': 'ITGlobal'},
    {'id': 78638, 'name': 'Тинькофф'},
    {'id': 1057, 'name': 'Лаборатория Касперского'},
    {'id': 1740, 'name': 'Яндекс'},
    {'id': 2381, 'name': 'Softline'},
    {'id': 3776, 'name': 'МТС'},
    {'id': 906557, 'name': 'SberTech'},
    {'id': 1122462, 'name': 'Skyeng'},
]
PARAMS: dict[str, bool | int] = {
    "per_page": 100,
    "only_with_salary": True
}
DATABASE_NAME = 'hh_vacancies'

def config(filename='database.ini', section='postgresql'):
    """Получение данных для работы БД из database.ini."""

    parser = ConfigParser()
    parser.read(filename)
    db = {}

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Некорректно заполненный файл database.ini')

    return db