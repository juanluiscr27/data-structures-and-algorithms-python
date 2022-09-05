# Array list Data Structure and algorithms with Python
from dsa.data_structures.array_list import ArrayList


def test_array_list():
    # Declare an Array list of 5 elements
    my_array_list = ArrayList(3)
    print(f"Is empty: {my_array_list.is_empty()}")
    # Adding elements to the Array list
    print("Adding elements...")
    my_array_list.insert(5)
    my_array_list.insert(10)
    my_array_list.insert(8)
    my_array_list.insert(4)
    my_array_list.insert(7)
    my_array_list.remove_at(2)
    # Looping through all the elements
    for index in range(my_array_list.size):
        print(my_array_list.get(index))

    print(f"Index of 8: {my_array_list.index_of(8)}")
    print(f"Contains 10? {my_array_list.contains(10)}")
    print(f"Is empty: {my_array_list.is_empty()}")


if __name__ == '__main__':
    test_array_list()
