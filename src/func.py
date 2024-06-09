import json


def get_data(file_='../operations.json'):
    """Читает и возвращает список данных из файла operations.json."""
    with open(file_, 'r', encoding='utf-8') as file:
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
