# Array Data Structure and algorithms with Python
from dsa.data_structures.array import Array


def test_array():
    # Declare an Array of 5 elements
    my_array = Array(5)
    # Adding elements to the Array
    my_array.insert_at(0, 5)
    my_array.insert_at(1, 10)
    my_array.insert_at(2, 8)
    my_array.insert_at(3, 4)
    my_array.insert_at(4, 7)
    # Looping through all the elements
    for index in range(my_array.length):
        print(my_array.get(index))


if __name__ == '__main__':
    test_array()
