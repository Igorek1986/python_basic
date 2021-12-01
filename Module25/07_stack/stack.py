class Stack:

    # TODO, т.к. этот список относится только к одному объекту класса, стоит реализовать его в метода __init__.
    stack = []

    def add_stack(self, obj):
        self.stack.append(obj)

    def del_stack(self):
        self.stack.pop()

    def __str__(self):

        # TODO, стоит реализовать цикл по списку, для создания строки со значениям текущего списка stack.

        return f'{self.stack}'
