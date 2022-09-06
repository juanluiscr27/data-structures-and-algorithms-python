from dsa.data_structures.linked_list import LinkedList


class Stack:
    """
    This code defines a Stack class implemented with Linked list and a limit capacity
    :param size: Max size of the Stack
    """
    def __init__(self, size):
        if size < 0:
            raise AttributeError("Stack size cannot be negative")

        self._items = LinkedList()
        self.capacity = size
        self.top = -1

    def __str__(self):
        return str(self._items)

    def is_empty(self):
        """
        Check if the Stack has items in it or is empty
        :return: True if the Stack top field is pointing to no item, otherwise False
        """
        return self.top == -1

    def is_full(self):
        """

        :return:
        """
        return self.top == self.capacity - 1

    def push(self, item):
        """

        :param item:
        """
        if self.is_full():
            raise StackOverFlowError("Stack is full")

        self._items.add_last(item)
        self.top += 1

    def pop(self):
        """

        :return:
        """
        if self.is_empty():
            raise StackEmptyError("Stack is empty")

        last_item = self.peek()
        self._items.remove_last()
        self.top -= 1
        return last_item

    def peek(self):
        """

        :return:
        """
        if self.is_empty():
            raise StackEmptyError("Stack is empty")

        last_item = self._items.get(self.top)
        return last_item.value

    def search(self, item):
        """

        :param item:
        :return:
        """
        return self._items.index_of(item)


class StackOverFlowError(Exception):
    """
    Raised when adding a new item and the stack is full.
    """
    pass


class StackEmptyError(Exception):
    """
    Raised when removing an item and the stack is empty.
    """
    pass
