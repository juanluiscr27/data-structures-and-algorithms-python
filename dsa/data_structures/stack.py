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
        Check if the Stack has no items in it
        :return: True if the Stack top field is pointing to no item, otherwise False
        """
        return self.top == -1

    def is_full(self):
        """
        Check if the Stack has filled its capacity
        :return: True if the Stack top field is pointing to the higher possible index, otherwise False
        """
        return self.top == self.capacity - 1

    def push(self, item):
        """
        Inserts an element at the top of the Stack
        Inserts a new element with constant O(1) time complexity
        :param item: element to insert
        :raise: StackOverFlowError if the Stack is full at the moment of insertion
        """
        if self.is_full():
            raise StackOverFlowError("Stack is full")

        self._items.add_last(item)
        self.top += 1

    def pop(self):
        """
        Removes the element at the top of the Stack
        Removes the last element with linear O(n) time complexity
        :return: The item removed
        :raise: StackEmptyError if the Stack is empty at the moment of deletion
        """
        if self.is_empty():
            raise StackEmptyError("Stack is empty")

        last_item = self.peek()
        self._items.remove_last()
        self.top -= 1
        return last_item

    def peek(self):
        """
        Retrieves the value of the item at the top of the Stack
        :return: The value of the last element
        :raise: StackEmptyError if the Stack is empty at the moment of retrieval
        """
        if self.is_empty():
            raise StackEmptyError("Stack is empty")

        last_item = self._items.get(self.top)
        return last_item

    def search(self, item):
        """
        Look up an element is present in the Stack and returns its position
        Traverses the Stack with linear O(n) time complexity
        :param item: Element to search for
        :return: The element index if exist or -1 if not
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
