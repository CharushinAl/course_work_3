# Импорт функций и константы
from utils.utils import OPERATIONS_PATH, load_json, number_masking, executed_operation, form_date, sort_operations


def main():
    # Загружаем из файла JSON в json_list
    json_list = load_json(OPERATIONS_PATH)
    # Сортируем список записывая выполненые операции в json_executed
    json_executed = executed_operation(json_list)
    # Сортируем список выполненых операций по дате в json_sort
    # Оставляем 5 последних обрезая список
    json_sort = sort_operations(json_executed)[:5]

    # Вывод 5 последних операций в заданном формате
    for op in json_sort:
        print(f'{form_date(op["date"])} {op["description"]}')
        if op.get('from'):
            print(f'{number_masking(op["from"])} -> {number_masking(op["to"])}')
        else:
            print(f'-> {number_masking(op["to"])}')
        print(f'{op["operationAmount"]["amount"]} {op["operationAmount"]["currency"]["name"]}')


# Вызов главной функции
main()
