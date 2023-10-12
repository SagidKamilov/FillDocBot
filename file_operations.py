import os
from typing import List, Dict

from contract_fill import fill_doc

path_to_doc = r"Contracts/docs"
find_files_name_file = "file_name"
find_files_path_to_file = "path_to_file"


def delete_file(file_name) -> str | FileNotFoundError:
    """
    Удаляет указанный файл.

    :param: file_name - имя файла, которого надо удалить
    :return: Строка с сообщением об успешном удалении или исключение FileNotFoundError в случае отсутствия файла.
    """
    try:
        path_to_file = path_to_doc + file_name
        os.remove(path_to_file)
        return "Удаление файла прошло успешно!"
    except FileNotFoundError as error:
        raise error


def delete_files(path_to_dir: str) -> str:
    """
    Удаляет все файлы в указанной директории.

    :param path_to_dir: Путь к директории для удаления файлов.
    :return: Строка об успешном удалении
    """
    try:
        files = os.scandir(path_to_dir)
        for file in files:
            file_path = str(file)
            delete_file(file_path)
        return "Удаление прошло успешно!"
    except FileNotFoundError as error:
        raise error


def find_files() -> List[Dict[str, str]] | str:
    """
    Поиск и возврат списка имен файлов в указанной директории.

    :param: None
    :return: Список пар ключ-значений - {"file_name": "<имя_файла>", "path_to_file": "<путь_к_файлу>"}
    """
    try:
        files = os.scandir(path_to_doc)
        names_files = [
            {find_files_name_file: file.name, find_files_path_to_file: file.path} for file in files
        ]
        return names_files
    except FileNotFoundError as error:
        return "Файл на обнаружен"


info = {
    "flight": "Елабуга-Яблоновский",
    "template": "Б",
    "date": "02.10.2023",
    "from_address": "3",
    "from_date": "4",
    "contact_person_from": "5",
    "contact_person_from_phone": "6",

    "to_address": "7",
    "to_date": "8",
    "contact_person_to": "9",
    "contact_person_to_phone": "10",

    "type_machine": "11",
    "name_cargo": "12",
    "type_loading": "13",
    "type_unloading": "14",
    "vat": "15",
    "car_number": "16",
    "car_model": "17",
    "trailer_number": "18",
    "trailer_model": "19",

    "name_driver": "20",
    "phone_driver": "21",
    "passport_driver": "22",
    "contact_manager": "23",
    "code_ati": "24",

    "price_customer": "23",
    "info_customer": "23",
    "full_org_name_customer": "23",
    "short_org_name_customer": "23",

    "price_driver": "12323",
    "carrier_info": "Паспорт",
    "full_org_name_carrier": "23",
    "short_org_name_carrier": "23"
}
fill_doc(info)