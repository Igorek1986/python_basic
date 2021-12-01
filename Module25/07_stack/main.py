class Stack:
    stack = []

    def add_stack(self, obj):
        self.stack.append(obj)

    def del_stack(self):
        self.stack.pop()

    def __str__(self):
        return f'{self.stack}'


class TaskManager:
    task_manager = {}

    def __str__(self):
        return f'{self.task_manager}'

    def new_task(self, task, num):

        if num not in self.task_manager:
            self.task_manager[num] = Stack()
        self.task_manager[num].add_stack(task)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
# print(Stack())

print(manager)
