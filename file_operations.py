import os
from typing import List, Dict


path_to_doc = r"Contracts/docs/"
FindFiles_NameFile = "file_name"
FindFiles_PathFile = "file_path"
FindFiles_ShortNameFile = "short_file_name"


def extract(file_name: str) -> str:
    """
    Функция получает полезную информацию из имени документа.

    :param: file_name: имя файла для преобразования
    :return: short_file_name: полезная информация в виде строки
    """
    extract_meta_data: list = file_name.replace(".docx", "").split("_")
    type_cotract: str = extract_meta_data[1]
    flight: str = extract_meta_data[2]
    flight_date: str = extract_meta_data[3]
    template_doc: str = extract_meta_data[4]
    short_file_name: str = f"{type_cotract[0]}_{flight}_{flight_date}_{template_doc}"
    return short_file_name


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
            file_path = str(file.name)
            delete_file(file_path)
        return "Все контракты были удалены"
    except FileNotFoundError as error:
        raise error


def find_files() -> List[Dict[str, str]] | str:
    """
    Поиск и возврат списка имен файлов в указанной директории.

    :param: None
    :return: Список пар ключ-значений - {"file_name": "<имя_файла>", "file": "<короткое имя файла>"}
    """
    try:
        files = os.scandir(path_to_doc)
        names_files = [
            {FindFiles_PathFile: file.path, FindFiles_NameFile: file.name, FindFiles_ShortNameFile: extract(file.name)} for file in files
        ]
        return names_files
    except FileNotFoundError as error:
        return "Файл на обнаружен"

