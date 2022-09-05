
class Array:
    """
    This code defines a static Array class.
    It contains a length property, an access method and an insert method
    :param length: Array size
    :param args: Initialization values (optional)
    """

    def __init__(self, length: int, *args):
        if len(args):
            self.length = len(args)
            self._values = list(args)
            self._values.insert(0, length)
        else:
            self.length = length
            self._values = [0 for _ in range(length)]

    def insert_at(self, index: int, value) -> None:
        """
        Inserts a new item to the array at a given position.
        Access an element and assign a value with constant O(1) time complexity
        :param index: Position to insert
        :param value: Value to insert
        :raise: IndexError if the given index is not part of the array
        """
        if 0 <= index < self.length:
            self._values[index] = value
        else:
            raise IndexError("Array index out of range")

    def get(self, index: int):
        """
        Retrieves an element in the array at the given index position.
        Access an element and read a value with constant O(1) time complexity
        :param index: Position to retrieve
        :return: The value of the element at given index
        :raise: IndexError if the given index is not part of the array
        """
        if 0 <= index < self.length:
            return self._values[index]
        else:
            raise IndexError("Array index out of range")
