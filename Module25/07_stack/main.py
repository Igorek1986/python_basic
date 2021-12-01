from stack import Stack


class TaskManager:
    # TODO, т.к. этот список относится только к одному объекту класса, стоит реализовать его в метода __init__.
    task_manager = {}

    def __str__(self):
        # TODO, после того, как метод __str__ класса Stack будет реализован,
        #  Предлагаю создать цикл по словарю task_manager, внутри которого, необходимо собрать строку для возврата при помощи return.
        return ''

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

# TODO, цикл ниже получился лишним
for i in Stack.stack:
    print(i)

print(manager)
