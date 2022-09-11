
class Queue:
    """
    This code defines a Simple Queue class implemented using Linked list with limit capacity
    :param size: Max size of the Queue
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
            raise AttributeError("Queue size cannot be negative")

        self.capacity = size
        self.front = None
        self.rear = None
        self.size = 0

    def __str__(self):
        values = []
        current_node = self.front
        while current_node:
            values.append(current_node.value)
            current_node = current_node.next

        return str(values)

    def is_empty(self):
        """
        Check if the Queue has no items in it
        :return: True if the Queue front field is pointing to no item, otherwise False
        """
        return self.front is None

    def is_full(self):
        """
        Check if the Queue has filled its capacity
        :return: True if the Queue size field equals the Queue capacity, otherwise False
        """
        return self.size == self.capacity

    def enqueue(self, item):
        """
        Inserts an element at the end of the Queue (The tail of the Linked list).
        Adds the new item with constant O(1) time complexity
        :param item: element to insert
        :raise: QueueOverFlowError if the Queue is full at the moment of insertion
        """
        if self.is_full():
            raise QueueOverFlowError("Queue is full")

        new_node = self.Node(item)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
            self.size += 1
            return

        self.rear.set_next(new_node)
        self.rear = new_node
        self.size += 1

    def dequeue(self):
        """
        Retrieves and removes the element at the front of the Queue (The head of the Linked list).
        Removes the first element with constant O(1) time complexity
        :return: The item removed
        :raise: QueueEmptyError if the Queue is empty at the moment of deletion
        """
        if self.is_empty():
            raise QueueEmptyError("Queue is empty")

        first_item = self.front
        self.front = first_item.next
        self.size -= 1
        return first_item.value

    def peek(self):
        """
        Retrieves the value of the item at the front of the Queue
        Access the first element with constant O(1) time complexity
        :return: The value of the first element
        :raise: QueueEmptyError if the Queue is empty at the moment of retrieval
        """
        if self.is_empty():
            raise QueueEmptyError("Queue is empty")

        return self.front.value

    def search(self, item):
        """
        Look up an element is present in the Queue and returns its position
        Traverses the Queue with linear O(n) time complexity
        :param item: Element to search for
        :return: The element index if exist or -1 if not
        """
        counter = 0
        current_node = self.front
        while current_node:
            if current_node.value == item:
                return counter

            current_node = current_node.next
            counter += 1
        return -1


class QueueOverFlowError(Exception):
    """
    Raised when adding a new item and the queue is full.
    """
    pass


class QueueEmptyError(Exception):
    """
    Raised when removing an item and the queue is empty.
    """
    pass
