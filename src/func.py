import json


def get_data():
    """Читает и возвращает список данных из файла operations.json."""
    with open('../operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def sort_data(data):
    """Возвращает отсортированный список по полю state=EXECUTED и по дате."""
    alt_data = []
    for i in data:
        if i.get('state') == 'EXECUTED':
            alt_data.append(i)
    alt_data.sort(key=lambda x: x.get('date'), reverse=1)
    return alt_data


def transform_date(data):
    """Возвращает дату в нужном формате."""
    date = '.'.join(data['date'].split('T')[0].split('-')[::-1])
    return date


def mask_data(bank_number):
    """Маскирует и озвращает номера счетов и карт."""
    if bank_number is None:
        return ""
    elif len(bank_number) == 25:
        return bank_number[:5] + 'XXXXXXXXXXXXXXXX' + bank_number[-4:]
    return bank_number[:-16]+'XXXX XX'+bank_number[-10:-8]+' '+bank_number[-8:-4]+' XXXX'


def print_data(data, date, from_, to_):
    """"Возвращает данные об операции в нужном формате для печати."""
    return (f"{date} {data.get('description')}\n"
            f"{from_} => {to_}\n"
            f"{data.get('operationAmount')['amount']} "
            f"{data.get('operationAmount')['currency']['name']}\n")
