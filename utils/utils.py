import json
import os

OPERATIONS_PATH = os.path.join('data', 'operations.json')


def load_json(file_name: str):
    """
    Загружает операции из JSON
    :return: list of dictionaries.
    """
    with open(file_name, 'r') as f:
        operations = json.load(f)
    return operations


def form_date(date):
    """
    Меняет формат даты.
    :param date: string.
    :return: string format dd.mm.yy

    """
    date_dmy = date.split('T')[0]
    year, month, day = date_dmy.split('-')

    return f'{day}.{month}.{year}'


def number_masking(operation_data: str):
    """

    :param operation_data:
    :return:
    """
    if operation_data:

        op_type = " ".join(operation_data.split()[:-1])
        op_number = operation_data.split()[-1]

    if len(op_number) == 16:
        number = f'{op_number[0:4]} {op_number[4:6]}** **** {op_number[12:]}'

        return f'{op_type} {number}'

    elif len(op_number) == 20:
        number = f'**{op_number[16:]}'

        return f'{op_type} {number}'

    return "N/A"


def sort_operations(json=None):
    """
    Сортирует список операций по дате.
    :param json_dicts: list
    :return: list
    """
    sort_list = sorted(json, key=lambda x: x.get("date"), reverse=True)

    return sort_list


def executed_operation(sort_list: list) -> list:
    """
    :param sort_list: list
    :return: list
    """
    executed_op = [op for op in sort_list if 'state' in op and op["state"] == "EXECUTED"]

    return executed_op
