from utils.utils import load_json, form_date, number_masking, sort_operations, executed_operation
import json


def test_load_json():
    # Тестовый файл JSON
    test_file = './test.json'

    # Создание тестовых данных
    test_data = {
        "id": 9,
        "state": "E",
        "date": "2018-06-30"
    }

    with open(test_file, 'w') as file:
        json.dump(test_data, file)

    # Вызываем функцию load_json с тестовым файлом
    result = load_json(test_file)

    # Проверяем, что результат соответствует ожидаемым данным
    assert isinstance(result, dict), "Результат должен быть словарем"
    assert result == test_data, "Содержимое файла JSON не совпадает с ожидаемым"

    print("Тестирование функции read_json_file() успешно завершено.")


test_load_json()


def test_form_date():
    # Подготовка тестовых данных
    input_date = "2023-05-15T10:30:00"
    expected_output = "15.05.2023"

    # Вызов функции form_date с тестовыми данными
    result = form_date(input_date)

    # Проверка результата
    assert result == expected_output


test_form_date()


def test_number_masking():
    # Создаем тестовые данные
    test_cases = [
        ("Счет 44812258784861134719", "Счет **4719"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Maestro 3928549031574026", "Maestro 3928 54** **** 4026"),
    ]

    # Проверяем, что номер карты/счета маскируется в соответствии с требованиями
    for test_input, expected_output in test_cases:
        result = number_masking(test_input)
        assert result == expected_output, "Вывод совпадает с ожидаемым"


test_number_masking()


def test_sort_operations():
    # Создаем тестовые данные
    transactions = [
        {"date": "2023-05-15", "amount": 100},
        {"date": "2023-05-13", "amount": 200},
        {"date": "2023-05-16", "amount": 150},
    ]

    # Вызываем функцию sort_operations для сортировки
    sorted_transactions = sort_operations(transactions)

    # Проверяем, что список отсортирован по убыванию даты
    assert sorted_transactions == [
        {"date": "2023-05-16", "amount": 150},
        {"date": "2023-05-15", "amount": 100},
        {"date": "2023-05-13", "amount": 200},
    ]


test_sort_operations()


def test_executed_operation():
    # Создаем тестовые данные
    operations = [
        {"state": "EXECUTED", "amount": 100},
        {"state": "PENDING", "amount": 200},
        {"state": "EXECUTED", "amount": 150},
    ]

    # Вызываем функцию executed_operation для фильтрации выполненных операций
    executed_operations = executed_operation(operations)

    # Проверяем, что в результате остались только выполненные операции
    assert executed_operations == [
        {"state": "EXECUTED", "amount": 100},
        {"state": "EXECUTED", "amount": 150},
    ]


test_executed_operation()
