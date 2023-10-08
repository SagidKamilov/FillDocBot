import os

path_dir = r"C:\Users\89615\Desktop\FillDocBot\Contracts\docs"


def delete_file(file: str) -> str:
    if file:
        try:
            os.remove(file)
            return "Удаление прошло успешно!"
        except Exception as error:
            return f"Ошибка удаления - {error}"
    else:
        return "Файл не найден"


def delete_files(path_to_dir):
    if path_to_dir:
        try:
            for file in os.scandir(path_to_dir):
                delete_file(file)
        except Exception as error:
            return f"Ошибка удаления - {error}"
    else:
        return "Путь к файлу не найден"


def check_exists_files(path_to_dir):
    if path_to_dir:
        for file in os.scandir(path_to_dir):
            yield file.path
    else:
        return "Файл не найден"

