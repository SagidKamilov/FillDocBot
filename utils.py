import re


def check_date(date):
    return True if re.match(r"\d{2}\.\d{2}\.\d{4}", date) else False
