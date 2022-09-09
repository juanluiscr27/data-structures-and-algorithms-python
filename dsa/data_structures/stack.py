from dsa.data_structures.linked_list import LinkedList


class Stack:
    """
    This code defines a Stack class implemented with Linked list and a limit capacity
    :param size: Max size of the Stack
    """

    class Node:
        """
        This code defines a Node class.
        :param value: Data content of the Node
        """

        def __init__(self, value):
            self.value = value
            self.next = None

        def set_next(self, next_node):
            """
            Adds the address to the subsequent Node as a reference
            :param next_node: The next Node reference
            """
            self.next = next_node

        def remove_next(self):
            """
            Deletes the reference to next Node
            :return: The Node removed from the address field
            """
            next_node = self.next
            self.next = None
            return next_node

        def update_value(self, new_value):
            """
            Change the value on the Node data field
            :param new_value: The new value to set on the Node
            """
            self.value = new_value

    def __init__(self, size):
        if size < 0:
            raise AttributeError("Stack size cannot be negative")

        self.capacity = size
        self.top = None
        self.size = 0

    def __str__(self):
        values = []
        current_node = self.top
        while current_node:
            values.insert(0, current_node.value)
            current_node = current_node.next

        return str(values)

    def is_empty(self):
        """
        Check if the Stack has no items in it
        :return: True if the Stack top field is pointing to no item, otherwise False
        """
        return self.top is None

    def is_full(self):
        """
        Check if the Stack has filled its capacity
        :return: True if the Stack top field is pointing to the higher possible index, otherwise False
        """
        return self.size == self.capacity

    def push(self, item):
        """
        Inserts an element at the top of the Stack
        Inserts a new element with constant O(1) time complexity
        :param item: element to insert
        :raise: StackOverFlowError if the Stack is full at the moment of insertion
        """
        if self.is_full():
            raise StackOverFlowError("Stack is full")

        new_item = self.Node(item)
        new_item.next = self.top
        self.top = new_item
        self.size += 1

    def pop(self):
        """
        Removes the element at the top of the Stack
        Removes the last element with constant O(1) time complexity
        :return: The item removed
        :raise: StackEmptyError if the Stack is empty at the moment of deletion
        """
        if self.is_empty():
            raise StackEmptyError("Stack is empty")

        last_item = self.top
        self.top = last_item.remove_next()
        self.size -= 1
        return last_item.value

    def peek(self):
        """
        Retrieves the value of the item at the top of the Stack
        :return: The value of the last element
        :raise: StackEmptyError if the Stack is empty at the moment of retrieval
        """
        if self.is_empty():
            raise StackEmptyError("Stack is empty")

        return self.top.value

    def search(self, item):
        """
        Look up an element is present in the Stack and returns its position
        Traverses the Stack with linear O(n) time complexity
        :param item: Element to search for
        :return: The element index if exist or -1 if not
        """
        counter = 0
        current_node = self.top
        while current_node:
            if current_node.value == item:
                return counter

            current_node = current_node.next
            counter += 1
        return -1


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
