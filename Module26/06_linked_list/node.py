class Node:
    def __init__(self, num=None, num_next=None):
        self.num = num
        self.num_next = num_next

    def get_num(self):
        return self.num

    def get_num_next(self):
        return self.num_next

    def set_num(self, num):
        self.num = num

    def set_num_next(self, num_next):
        self.num_next = num_next
