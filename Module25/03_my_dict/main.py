class MyDict(dict):
    def get(self, key):
        return super().get(key, 0)


my_dict = MyDict({'a': 1})
print(my_dict.get('b'))
print(my_dict.get('a'))
