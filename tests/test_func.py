from src.func import get_data, sort_data, transform_date, mask_data

def test_get_data():
    test_path = 'tests/test_operations.json'
    test_data = get_data(test_path)
    print(test_data)
    assert test_data == [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}]


def test_sort_data():
    assert sort_data([{'id': 441945886, 'state': 'EXECUTED'},{'id': 441945886, 'state': 'CANCELED'}]) == [{'id': 441945886, 'state': 'EXECUTED'}]


def test_transform_date():
    assert transform_date({"date": "2019-08-26T10:50:58.294041"}) == '26.08.2019'


def test_mask_data():
    assert mask_data(None) == ""
    assert mask_data('Счет 90424923579946435907') == 'Счет XXXXXXXXXXXXXXXX5907'
    assert mask_data('Visa Classic 2842878893689012') == 'Visa Classic XXXX XX88 9368 XXXX'
