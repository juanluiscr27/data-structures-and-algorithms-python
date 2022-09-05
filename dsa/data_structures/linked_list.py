class Node:
    """
    This code defines a Node class.
    It contains a value and a next property with the address to subsequent Node, if any
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


class LinkedList:
    """
    This code defines a LinkedList class.
    It contains a list of nodes.
    Also, has convenient methods to add, delete, search and access values.
    """

    def __init__(self):
        self._head = None
        self._tail = None
        self.size = 0

    def __str__(self):
        values = []
        current_node = self._head
        while current_node:
            values.append(current_node.value)
            current_node = current_node.next

        return str(values)

    def is_empty(self) -> bool:
        """
        Check if the LinkedList has elements or is empty
        :return: True if the LinkedList has no first element, otherwise False
        """
        return self._head is None

    def add_at(self, index, value):
        """
        Inserts a new element to the LinkedList at a given position.
        Creates a new Node pointing to the Node after the given position and
        set the Node previous the given index to reference the new Node.
        Connects a new Node with a linear O(n) time complexity
        :param index: Position to insert the Node
        :param value: Value of the Node
        :raise: IndexError if the given index is not in the range of the LinkedList
        """
        if self.is_empty() or 0 > index or index > self.size:
            raise IndexError("LinkedList index out of range")
        if index == 0:
            self.add_first(value)
            return
        if index == self.size:
            self.add_last(value)
            return

        counter = 1
        previous_node = self._head
        current_node = previous_node.next
        while current_node:
            if counter == index:
                new_node = Node(value)
                new_node.set_next(current_node)
                previous_node.set_next(new_node)
                self.size += 1
                return

            previous_node = current_node
            current_node = current_node.next
            counter += 1

    def add_first(self, value):
        """
        Inserts an element with a given value at the beginning of the list
        and set its address field to point to the previous first.
        If the list is empty the first element is the same as the last
        :param value: Value of the Node
        """
        new_node = Node(value)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node.set_next(self._head)
            self._head = new_node
        self.size += 1

    def add_last(self, value):
        """
        Inserts an element with a given value at the end of the list
        and set the address field of the previous last to point to this.
        If the list is empty the last element is the same as the first
        :param value: Value of the Node
        """
        new_node = Node(value)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.set_next(new_node)
            self._tail = new_node
        self.size += 1

    def remove_at(self, index):
        """
        Deletes an element from the LinkedList at a given position.
        Set the Node previous the given index to point the Node after that and
        Remove the element references and connections.
        Disconnects a Node with a linear O(n) time complexity
        :param index: Position of the element to remove
        :raise: IndexError if the given index is not in the range of the LinkedList
        """
        if self.is_empty() or 0 > index or index >= self.size:
            raise IndexError("LinkedList index out of range")
        if index == 0:
            self.remove_first()
            return
        if index == self.size - 1:
            self.remove_last()
            return

        counter = 1
        previous_node = self._head
        current_node = previous_node.next
        while current_node:
            if counter == index:
                next_node = current_node.remove_next()
                previous_node.set_next(next_node)
                self.size -= 1
                return

            previous_node = current_node
            current_node = current_node.next
            counter += 1

    def remove_first(self):
        """
        Deletes the element at the beginning of the list and set the list `head` field
        to point to the previous second element.
        If the list has only one Node the first and the last element are removed
        :return: None
        :raise: NoSuchElementError if the list is empty
        """
        if self.is_empty():
            raise NoSuchElementError("No more elements in the list")
        if self._head == self._tail:
            self._head = None
            self._tail = None
            self.size = 0
            return

        new_head = self._head.remove_next()
        self._head = new_head
        self.size -= 1

    def remove_last(self):
        """
        Deletes the element at the end of the list and set the list `tail` field
        to point to the Node previous the last.
        If the list has only one Node the first and the last element are removed
        :return: None
        :raise: NoSuchElementError if the list is empty
        """
        if self.is_empty():
            raise NoSuchElementError("No more elements in the list")
        if self._head == self._tail:
            self._head = None
            self._tail = None
            self.size = 0
            return

        previous_node = self._head
        current_node = previous_node.next
        while current_node.next:
            previous_node = current_node
            current_node = current_node.next

        previous_node.remove_next()
        self._tail = previous_node
        self.size -= 1

    def replace(self, index: int, value):
        """
        Updates the element in the list at a given position.
        Traverse the list and override the value of the element at the given position
        with linear O(n) time complexity
        :param index: The position of the element to update
        :param value: The new value to set on the element
        :raise: IndexError if the given index is larger than the ArrayList size
        or is a negative integer
        """
        if self.is_empty() or 0 > index or index > self.size:
            raise IndexError("LinkedList index out of range")

        counter = 0
        current_node = self._head
        while current_node:
            if counter == index:
                current_node.update_value(value)
                return

            current_node = current_node.next
            counter += 1

    def index_of(self, value) -> int:
        """
        Searches for the first element with a given value and returns its position in
        the LinkedList, or -1 if the list does not contain the value.
        Traverses the LinkedList with linear O(n) time complexity
        :param value: The value to look up
        :return: The element index if exist or -1 if not
        """
        index = 0
        current_node = self._head
        while current_node:
            if current_node.value == value:
                return index
            index += 1
            current_node = current_node.next

        return -1

    def contains(self, value) -> bool:
        """
        Searches for a given value in the LinkedList and returns True if the list contains
        at least one occurrence of the value.
        Traverses the LinkedList with linear O(n) time complexity
        :param value: The value to look up
        :return: True if the LinkedList contains the specified value, otherwise False
        """
        return self.index_of(value) != -1


class NoSuchElementError(Exception):
    """
    Raised when there are no more elements in the list.
    """
    pass
