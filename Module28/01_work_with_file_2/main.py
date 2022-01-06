from typing import TextIO


class File:
    """ Context Manager File """

    def __init__(self, file_name: str, method: str) -> None:
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


with File('example.txt', 'r') as file:
    file.write('Всем привет!\n')
