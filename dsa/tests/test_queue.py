# Linked L=list Data Structure and algorithms with Python
from dsa.data_structures.queue import Queue


def test_queue():
    # Declare a Queue of 5 elements
    my_queue = Queue(5)
    # Adding elements to the Queue
    print(f"Queue is empty: {my_queue.is_empty()}")
    my_queue.enqueue(5)
    my_queue.enqueue(10)
    my_queue.enqueue(8)
    print(f"Peek item: {my_queue.peek()}")
    # Print all the elements
    print(my_queue)
    my_queue.enqueue(4)
    my_queue.enqueue(7)
    print(f"Queue is empty: {my_queue.is_empty()}")
    print(my_queue)
    print(f"Queue is full: {my_queue.is_full()}")
    # my_queue.enqueue(20)
    print(f"Search 10: {my_queue.search(10)}")
    my_queue.dequeue()
    my_queue.dequeue()
    my_queue.dequeue()
    my_queue.dequeue()
    print(f"Item dequeued: {my_queue.dequeue()}")
    # my_queue.dequeue()
    print(f"Queue is empty: {my_queue.is_empty()}")
    print(f"Queue is full: {my_queue.is_full()}")


if __name__ == '__main__':
    test_queue()
