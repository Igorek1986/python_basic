from typing import TextIO


class File:
    """ Context Manager File """

    def __init__(self, file_name: str, method: str) -> None:
        self.file_name = file_name
        self.method = method

    def __enter__(self) -> TextIO:
        try:
            self.file_obj = open(self.file_name, self.method, encoding='UTF-8')
        except FileNotFoundError:
            self.file_obj = open(self.file_name, 'w', encoding='UTF-8')
        else:
            self.file_obj = open(self.file_name, 'a', encoding='UTF-8')
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.file_obj.close()
        return True


with File('example.txt', 'r') as file:
    file.write('Всем привет!\n')
