# Linked L=list Data Structure and algorithms with Python
from dsa.data_structures.stack import Stack


def test_stack():
    # Declare a Stack of 5 elements
    my_stack = Stack(5)
    # Adding elements to the Stack
    print(f"Stack is empty: {my_stack.is_empty()}")
    my_stack.push(5)
    my_stack.push(10)
    my_stack.push(8)
    print(my_stack)
    print(f"Peek item: {my_stack.peek()}")
    my_stack.push(4)
    my_stack.push(7)
    print(f"Stack is full: {my_stack.is_full()}")
    print(f"Stack is empty: {my_stack.is_empty()}")
    # Print all the elements
    print(my_stack)
    print(f"Peek item: {my_stack.peek()}")
    # my_stack.push(20)
    print(f"Search 10: {my_stack.search(10)}")
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    print(f"Item popped: {my_stack.pop()}")
    # my_stack.pop()
    print(f"Stack is empty: {my_stack.is_empty()}")


if __name__ == '__main__':
    test_stack()
