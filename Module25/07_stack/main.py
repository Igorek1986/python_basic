from stack import Stack


class TaskManager:
    def __init__(self):
        self.task_manager = {}

    def __str__(self):
        display = []
        if self.task_manager:
            for i_num in sorted(self.task_manager.keys()):
                display.append(f'{i_num} {self.task_manager[i_num]}\n')
        return ''.join(display)

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


print(manager)
