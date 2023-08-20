# 1
# ---- 1.1 ----
# Array

# ---- 1.2 ----
# Linked List

# 2
class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        
    def set_data(self, data):
        self.__data = data
        
    def get_data(self):
        return self.__data
    
    def set_next(self, node):
        self.__next = node
        
    def get_next(self):
        return self.__next

class LinkedList:
    def __init__(self):
        self.__head = None
        
    def is_empty(self):
        return self.__head is None
    
    def add(self, item):
        node = Node(item)
        node.set_next(self.__head)
        self.__head = node

    def size(self):
        pass

    def remove(self):
        pass
        
    def __str__(self):
        if self.__head is None:
            return '[]'
        current = self.__head
        data = str(current.get_data())
        while not current.get_next() is None:
            current = current.get_next()
            data += ", " + str(current.get_data())
        return '[' + data + ']'

    def search(self, item):
        search_item = self.__head
        while search_item:
            if search_item.get_data() == item:
                return search_item
            else:
                return "There is no such item"
        return "error" 

    def __iter__(self):
        self.my_iter = self.__head
        return self

    def __next__(self):
        if self.my_iter > len(LinkedList):
            raise StopIteration


my_list = LinkedList()
my_list.is_empty()
# my_list.add(1)
# my_list.add(5)
# my_list.add(75)
# my_list.add(95)
my_list.is_empty()
print(my_list)