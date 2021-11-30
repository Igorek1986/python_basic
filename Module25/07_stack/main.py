class Stack:
    stack = []

    def add_stack(self, obj):
        self.stack.append(obj)

    def del_stack(self):
        del self.stack[-1]


class TaskManager:
    task_manager = {}

    def __str__(self):
        pass

    def new_task(self, task, num):
        self.task_manager[task] = num


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)

print(manager)
