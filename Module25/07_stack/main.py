class Stack:
    stack = []

    def add_stack(self, obj):
        self.stack.append(obj)

    def del_stack(self):
        del self.stack[-1]

    def __str__(self):
        return f'{self.stack}'


class TaskManager:
    task_manager = {}

    def __str__(self):
        pass

    def new_task(self, task, num):
        print(num)
        if num not in self.task_manager.keys():
            Stack.add_stack(Stack(), f'{num} {task}')
        else:
            self.task_manager[num] = Stack()


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
# manager.new_task("отдохнуть", 1)
# manager.new_task("поесть", 2)
# manager.new_task("сдать дз", 2)
print(Stack())

# print(manager)
