from dsa.data_structures.array import Array


class ArrayList:
    """
    This code defines a dynamic Array class.
    It contains a length property, an access method and a search method.
    Also, this class has an insert and remove method
    :param length: ArrayList initial capacity
    """

    def __init__(self, length: int):
        self._array = Array(length)
        self.size = 0

    def is_empty(self):
        """
        Check if the ArrayList has elements or is empty
        :return: True if the ArrayList size is 0, otherwise False
        """
        return self.size == 0

    def insert(self, value):
        """
        Adds a new element at the end of the ArrayList. If the ArrayList is at full capacity,
        then increase the capacity by 100%.
        Inserts the element with linear O(n) time complexity
        :param value: new element to insert in the ArrayList
        """
        if self.size == self._array.length:
            new_array = Array(self._array.length * 2)
            for index in range(self.size):
                new_array.insert_at(index, self._array.get(index))

            self._array = new_array

        self._array.insert_at(self.size, value)
        self.size += 1

    def remove_at(self, index: int):
        """
        Deletes an element from the ArrayList at the given index position and
        decrement the size of the ArrayList.
        When the index of the element to delete is not the last, shift the subsequent
        elements one position to the left to fill the gap.
        Removes the element with linear O(n) time complexity
        :param index: Position of the element to remove
        :raise: IndexError if the given index is larger than the ArrayList size
        or is a negative integer
        """
        if not 0 <= index < self.size:
            raise IndexError("ArrayList index out of range")
        if index < self.size - 1:
            for shift in range(index, self.size - 1):
                self._array.insert_at(shift, self._array.get(shift + 1))

        self.size -= 1

    def replace(self, index: int, value):
        """
        Updates the item in the array at a given position.
        Access an element and override a value with constant O(1) time complexity
        :param index: The position of the element to update
        :param value: The new value to set on the element
        :raise: IndexError if the given index is larger than the ArrayList size
        or is a negative integer
        """
        if 0 <= index < self.size:
            self._array.insert_at(index, value)
        else:
            raise IndexError("ArrayList index out of range")

    def index_of(self, value):
        """
        Searches for a given value and returns the index of its first occurrence in the ArrayList,
        or -1 if the ArrayList does not contain the value.
        Traverses the ArrayList with linear O(n) time complexity
        :param value: The value to look up
        :return: The value index if exist or -1 if not
        """
        for index in range(self._array.length):
            if self._array.get(index) == value:
                return index
        return -1

    def get(self, index: int):
        """
        Retrieves the value of the element at the specified index position.
        Access an element with constant O(1) time complexity
        :param index: Position to retrieve
        :return: The value of the element at given index
        :raise: IndexError if the given index is larger than the ArrayList size
        or is a negative integer
        """
        if 0 <= index < self.size:
            return self._array.get(index)
        else:
            raise IndexError("ArrayList index out of range")

    def contains(self, value):
        """
        Searches for a given value in the ArrayList and returns True if the list contains
        at least one occurrence of the value.
        Traverses the ArrayList with linear O(n) time complexity
        :param value: The value to look up
        :return: True if the ArrayList contains the specified value, otherwise False
        """
        return self.index_of(value) != -1
