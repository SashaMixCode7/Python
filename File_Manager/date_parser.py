# Задача 2024.08.19.09
#
# Создайте модуль `date_parser.py`
#
# И в нём создайте функцию `is_date` которая на вход получает строку а возвращает `bool`
#
# Требуемый формат `%Y-%m-%d`
#
# Возвращает `True` если строка с датой успешно спарсилась с требуемым форматом.
# Иначе `False`
# Задача 2024.08.19.12
#
# Переделайте функцию `is_date` в функцию `is_date_by_format` и сделайте так, чтобы она принимала формат на вход.
#
# Также создайте список `FORMATS` в котором будем хранить все возможные форматы дат.
#
# Пока у нас их два: с дефисом и с наклонной чертой.
# Задача 2024.08.19.13
#
# Создайте заново функцию `is_date` которая на вход принимает строку.
#
# Но в этот раз нужно вернуть `True` в случае если `is_date_by_format` вернёт `True` с каким-нибудь из форматов списка `FORMATS`


from datetime import datetime

FORMATS = ["%Y-%m-%d", "%Y/%m/%d", "%Y.%m.%d"]


def is_date_by_format(date: str, date_format: str) -> bool:
    try:
        datetime.strptime(date, date_format)
        return True
    except ValueError:
        return False



def is_date1(date: str) -> bool:
    return any([is_date_by_format(date, date_format) for date_format in FORMATS])
