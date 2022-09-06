# Linked L=list Data Structure and algorithms with Python
from dsa.data_structures.linked_list import LinkedList


def test_linked_list():
    # Declare a Linked list of 5 elements
    my_linked_list = LinkedList()
    # Adding elements to the list
    my_linked_list.add_first(5)
    my_linked_list.add_last(10)
    my_linked_list.add_at(0, 8)
    my_linked_list.add_at(3, 4)
    my_linked_list.add_first(7)
    my_linked_list.add_last(50)
    my_linked_list.remove_first()
    my_linked_list.remove_last()
    my_linked_list.add_at(2, 20)
    print(f"List size: {my_linked_list.size}")
    my_linked_list.remove_at(3)
    # Print all the elements
    print(my_linked_list)
    my_linked_list.replace(1, 9.97)
    print(f"Updated list: \n{my_linked_list}")

    print(f"Index of 8: {my_linked_list.index_of(5)}")
    print(f"Contains 10?: {my_linked_list.contains(8)}")


if __name__ == '__main__':
    test_linked_list()
