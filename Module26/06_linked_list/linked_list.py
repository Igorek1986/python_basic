from node import Node


# TODO, наследование от object получилось лишним, т.к. все классы в python по умолчанию являются объектами.
#  В решении текущего задания стоит написать пару классов
#  1. Node() - будет выступать в роли одного элемента списка, должен содержать в себе два аргумента:
#  - Ссылка на следующий элемент.
#  - Текущее значение.
#  2. LinkedList() - будет выступать в роли списка. У него должны быть такие аргументы, как:
#  - Начальный элемент списка,
#  - Длина списка.
#  Этот класс должен организовать взаимодействие классов Node внутри.
class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_node = self.head
        output = '['
        while cur_node:
            output += str(cur_node.get_num()) + ' '
            cur_node = cur_node.get_num_next()
        output = output[:-1]
        output += ']'
        return output

    def __iter__(self):
        cur_node = self.head
        while cur_node:
            yield cur_node.get_num()
            cur_node = cur_node.get_num_next()
        return self

    def append(self, num):
        new_node = Node(num)
        cur_node = self.head
        if not cur_node:
            self.head = new_node
            return
        while cur_node.get_num_next():
            cur_node = cur_node.get_num_next()
        cur_node.set_num_next(new_node)

    def get(self, index):
        cur_node = self.head
        count = 0
        while cur_node:
            if count == index:
                return cur_node.get_num()
            count += 1
            cur_node = cur_node.get_num_next()
        print('Индекс не входит в границы')

    def remove_back(self):
        cur_node = self.head
        while cur_node.get_num_next().get_num_next():
            cur_node = cur_node.get_num_next()
        cur_node.set_num_next(None)

    def remove_front(self):
        cur_node = self.head
        self.head = cur_node.get_num_next()

    def remove(self, index):
        cur_node = self.head
        count = 0
        while cur_node.get_num_next():
            if index == 0:
                self.remove_front()
                return
            elif count + 1 == index:
                the_node_to_remove = cur_node.get_num_next()
                the_node_after_removed = the_node_to_remove.get_num_next()
                cur_node.set_num_next(the_node_after_removed)
                return
            count += 1
            cur_node = cur_node.get_next()
        print('Индекс не входит в границы')
