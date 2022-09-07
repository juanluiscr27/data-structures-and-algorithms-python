from dsa.data_structures.linked_list import LinkedList


class Queue:
    """
    This code defines a Simple Queue class implemented with Linked list and a limit capacity
    :param size: Max size of the Queue
    """
    def __init__(self, size):
        if size < 0:
            raise AttributeError("Queue size cannot be negative")

        self._items = LinkedList()
        self.capacity = size
        self.front = -1
        self.rear = -1

    def __str__(self):
        return str(self._items)

    def is_empty(self):
        """
        Check if the Queue has no items in it
        :return: True if the Queue front field is pointing to no item or front index is greater than rear.
        Otherwise False
        """
        return self.front == -1 and self.rear == -1

    def is_full(self):
        """
        Check if the Queue has filled its capacity
        :return: True if the Queue top field is pointing to the higher possible index, otherwise False
        """
        return self.rear == self.capacity - 1 or self.front > self.rear

    def enqueue(self, item):
        """
        Inserts an element at the end of the Queue
        Inserts a new element with constant O(1) time complexity
        :param item: element to insert
        :raise: QueueOverFlowError if the Queue is full at the moment of insertion
        """
        if self.is_full():
            raise QueueOverFlowError("Queue is full")
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear += 1

        self._items.add_at(self.rear, item)

    def dequeue(self):
        """
        Retrieves and removes the element at the front of the Queue
        Removes the last element with constant O(1) time complexity
        :return: The item removed
        :raise: QueueEmptyError if the Queue is empty at the moment of deletion
        """
        if self.is_empty():
            raise QueueEmptyError("Queue is empty")

        last_item = self.peek()
        self._items.remove_last()
        self.front += 1
        return last_item

    def peek(self):
        """
        Retrieves the value of the item at the top of the Queue
        :return: The value of the last element
        :raise: QueueEmptyError if the Queue is empty at the moment of retrieval
        """
        if self.is_empty():
            raise QueueEmptyError("Queue is empty")

        last_item = self._items.get(self.rear)
        return last_item.value

    def search(self, item):
        """
        Look up an element is present in the Queue and returns its position
        Traverses the Queue with linear O(n) time complexity
        :param item: Element to search for
        :return: The element index if exist or -1 if not
        """
        return self._items.index_of(item)


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
