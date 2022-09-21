# Hash Table Data Structure and algorithms with Python
from dsa.data_structures.hash_table import HashTable


def test_hash_table():
    # Declare a Hash Table of 5 elements
    my_hash_table = HashTable(5)
    print(my_hash_table)
    # Adding elements to the Hash Table
    print(f"Hash Table is empty: {my_hash_table.is_empty()}")
    my_hash_table.put("Jimmy", 5)
    my_hash_table.put("Lucy", 10)
    my_hash_table.put("Zoe", 8)
    print(my_hash_table)
    my_hash_table.put("Max", 4)
    my_hash_table.put("Ada", 7)
    print(f"Hash Table is empty: {my_hash_table.is_empty()}")
    # # Print all the elements
    print(my_hash_table)
    print(my_hash_table.keys())
    print(my_hash_table.values())
    key = "Jimmy"
    print(f"{key} = {my_hash_table.get(key)}")
    my_hash_table.put("Tim", 20)
    print(f"Search Tom: {my_hash_table.get('Tom')}")
    my_hash_table.remove("Ada")
    my_hash_table.remove("Jimmy")
    my_hash_table.remove("Tim")
    my_hash_table.remove("Lucy")
    print(f"Item removed: {my_hash_table.remove('Zoe')}")
    my_hash_table.remove("Max")
    # my_hash_table.remove("Tom")
    print(my_hash_table)
    print(f"Hash Table is empty: {my_hash_table.is_empty()}")


if __name__ == '__main__':
    test_hash_table()
