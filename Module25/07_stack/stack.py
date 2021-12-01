class Stack:
    stack = []

    def add_stack(self, obj):
        self.stack.append(obj)

    def del_stack(self):
        self.stack.pop()

    def __str__(self):
        return f'{self.stack}'
