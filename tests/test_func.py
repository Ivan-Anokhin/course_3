from src.func import get_data, sort_data, transform_date, mask_data, print_data


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


def test_print_data():
    assert (print_data({'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582', 'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'}, '08.12.2019', '', 'Счет XXXXXXXXXXXXXXXX5907') ==
            f"08.12.2019 Открытие вклада"
            f" => Счет XXXXXXXXXXXXXXXX5907"
            f"41096.24 USD")