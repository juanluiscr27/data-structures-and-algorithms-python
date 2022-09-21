
class HashTable:
    """
    This code defines a Hash Table class implemented Separate chaining using Linked list.
    Uses dynamic resizing to increase its capacity and a load factor of 0.85
    :param size: Hash Table initial capacity
    """

    class Node:
        """
        This code defines a Hash Tabel Node class
        :param key: Key of the value in the Table
        :param value: Data content of the Node
        """

        def __init__(self, key, value):
            self.key = key
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

    def __init__(self, size=11):
        self.load_factor = 0.75
        self.capacity = self.get_next_prime(size)
        self._array = []
        self.clear()
        self.size = 0

    def __str__(self) -> str:
        hash_table = ""
        for bucket in self._array:
            current_node = bucket
            while current_node:
                hash_table += f"'{current_node.key}': {current_node.value}, "
                current_node = current_node.next

        return f"{{{hash_table[:-2]}}}"

    def is_empty(self):
        """
        Check if the Hash Table size equals zero
        :return: True if the Hash Table size field is 0, otherwise False
        """
        return self.size == 0

    @staticmethod
    def is_prime(number: int) -> bool:
        """
        Validate if a given number is prime checking if it is divisible by any odd
        integer less or equal to its squared root
        :param number: The given number
        :return: True if the number is only divisible by itself. Otherwise False
        """
        if number < 2:
            return False
        if number % 2 == 0:
            return False

        i = 3
        while i*i <= number:
            if number % i == 0:
                return False
            i += 2
        return True

    def get_next_prime(self, number: int) -> int:
        """
        Check if the input number is even; increment it by one to make it odd if so.
        Later check if the odd number is prime and increment it by two until find the
        next prime number
        :param number: Input number to check
        :return: The nearest higher prime number
        """
        if number % 2 == 0:
            number += 1
        while not self.is_prime(number):
            number += 2
        return number

    def hash(self, key) -> int:
        """
        Takes an input value and maps it to a hash code to generate an integer index
        :param key: Input key value
        :return: An index value
        """
        hash_code = 0
        for pos, char in enumerate(str(key), 1):
            hash_code += pos ** ord(char)

        index = hash_code % self.capacity
        return index

    def rehash(self):
        self.capacity = self.get_next_prime(self.capacity * 2)
        old_array = self._array
        self.clear()
        for bucket in old_array:
            current_node = bucket
            while current_node:
                self.put(current_node.key, current_node.value)
                current_node = current_node.next

    def clear(self):
        self._array = [None for _ in range(self.capacity)]
        self.size = 0

    def put(self, key, value):
        if key is None or value is None:
            return
        if self.size / self.capacity > self.load_factor:
            self.rehash()
        if self.replace(key, value):
            return

        index = self.hash(key)
        new_node = self.Node(key, value)
        if not self._array[index]:
            self._array[index] = new_node
        else:
            new_node.set_next(self._array[index])
            self._array[index] = new_node
        self.size += 1

    def get(self, key):
        index = self.hash(key)
        current_node = self._array[index]
        while current_node:
            if current_node.key == key:
                return current_node.value

            current_node = current_node.next
        return None

    def remove(self, key):
        index = self.hash(key)
        previous_node = None
        current_node = self._array[index]
        while current_node:
            if current_node.key == key and not previous_node:
                value = current_node.value
                next_node = current_node.remove_next()
                self._array[index] = next_node
                self.size -= 1
                return value
            if current_node.key == key and previous_node:
                value = current_node.value
                next_node = current_node.remove_next()
                previous_node.set_next(next_node)
                self.size -= 1
                return value
            previous_node = current_node
            current_node = current_node.next

        raise KeyError("No such key found in Hash Table")

    def replace(self, key, value):
        index = self.hash(key)
        current_node = self._array[index]
        while current_node:
            if current_node.key == key:
                current_node.update_value(value)
                return True

            current_node = current_node.next
        return False

    def keys(self):
        keys = []
        for bucket in self._array:
            current_node = bucket
            while current_node:
                keys.append(current_node.key)
                current_node = current_node.next

        return keys

    def values(self):
        values = []
        for bucket in self._array:
            current_node = bucket
            while current_node:
                values.append(current_node.value)
                current_node = current_node.next

        return values
