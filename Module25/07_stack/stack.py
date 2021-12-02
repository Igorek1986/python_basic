class Stack:

    def __init__(self):
        self.stack = []

    def __str__(self):
        return ';'.join(self.stack)
        # return f'{self.stack}'

    def add_stack(self, obj):
        self.stack.append(obj)

    def del_stack(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack.pop()
