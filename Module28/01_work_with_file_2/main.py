from typing import TextIO


class File:
    """ Context Manager File """

    def __init__(self, file_name: str, method: str) -> None:
        # TODO, метод __init__ это простой список аргументов класса.
        #  Открывать файл стоит в методе __enter__.
        try:
            self.file_obj = open(file_name, method)
        except FileNotFoundError:
            self.file_obj = open(file_name, 'w')
        else:
            self.file_obj = open(file_name, 'a')

    def __enter__(self) -> TextIO:
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.file_obj.close()
        # TODO, пожалуйста, не забывайте отрабатывать исключения, которые возникают при закрытии файла.


with File('example.txt', 'r') as file:
    file.write('Всем привет!\n')
