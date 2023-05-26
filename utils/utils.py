import json
import os

OPERATIONS_PATH = os.path.join('data', 'operations.json')


def load_json(file_name):
    """
    Load JSON file.
    :return: list of dictionaries.
    """
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def form_date(date):
    """
    Change date format
    :param date: string
    :return: string (format dd.mm.yy)
    """
    date_dmy = date.split('T')[0]
    year, month, day = date_dmy.split('-')

    return f'{day}.{month}.{year}'


def number_masking(operation_data):
    """
    Masks transaction data.
    :param operation_data: string
    :return: string
    """
    if operation_data:
        type_op = " ".join(operation_data.split()[:-1])
        number = operation_data.split()[-1]

    if len(number) == 16:
        number_mask = f'{number[0:4]} {number[4:6]}** **** {number[12:]}'

        return f'{type_op} {number_mask}'

    elif len(number) == 20:
        number_mask = f'**{number[16:]}'

        return f'{type_op} {number_mask}'

    return "N/A"


def sort_operations(json=None):
    """
    Sort transactions by date.
    :param json: list of dictionaries
    :return: list of dictionaries
    """
    sort_list = sorted(json, key=lambda x: x.get("date"), reverse=True)

    return sort_list


def executed_operation(sort_list):
    """
    Sorts and returns completed operations.
    :param sort_list: list of dictionaries
    :return: list of dictionaries
    """
    executed_op = [op for op in sort_list if 'state' in op and op["state"] == "EXECUTED"]

    return executed_op
