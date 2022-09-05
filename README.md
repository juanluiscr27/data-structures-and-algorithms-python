# Data Structure and Algorithms

----
A computer program is a collection of instructions to perform a specific task. For this, a computer 
program may need to store data, retrieve data, and perform computations on the data.

A data structure is a named location that is used to store and organize data. And, an algorithm is a 
set of steps or instructions for completing a task.

Algorithms normally work upon collections of data. To be correct, an algorithm should produce an 
expected result given a specific set of data.

Efficiency measure the time and space complexity of an algorithm when performing a task 
over a specific data structure. The metric to measure data structures and algorithms efficiency
is better known as Big O notation. 

Learning data structures and algorithms allow us to write efficient and optimized computer programs.

### Big O Notation
Big O Notation is a mathematical definition that describes the performance of an algorithm based on 
worst case scenario for the size of its argument. Big O refers to Order of magnitude of complexity 
(time or space) to measure the efficiency of an algorithm as its input data size grows.

Time complexity in computer terms indicates the run time an algorithm require to complete a
certain task. On the oder hand, space complexity refers to amount memory required by such algorithm.

Common values of algorithm complexity are, starting from the most efficient:
* O(1): Constant
* O(log n): Logarithmic
* O(n): Linear
* O(n log n): Quasi-linear
* O(n^2): Quadratic
* O(2^n): Exponential
* O(n!): Factorial

## Data Structures
Data structure is a storage that is used to store and organize data. It is a way of arranging data 
on a computer so that it can be accessed and updated efficiently.

The data can be organized in two ways either linear or non-linear way. There are two types of data 
structure available for the programming purpose:
* Primitive data structure
* Non-primitive data structure

### Primitive data structure 
Is a fundamental type of data structure that stores the data of only one type. Primitive data 
structure is a data structure that can hold a single value in a specific location. These data 
structures commonly are the data types which come with built-in support in the programming 
languages. For example, most of the languages provide the following built-in data types:
* Integers: The integer data type contains whole numbers that can be either negative or positive 
numeric values.
* Floating: The float is a data type that can hold decimal values.
* Boolean: It is a data type that can hold either a `True` or a `False` value.
* Character: It is a data type that can hold a single character value both uppercase and lowercase.

### Non-primitive data structure
The non-primitive data structure is a type of data structure which is a user-defined that stores 
the data of different types in a single entity. Non-primitive data structure, it is categorized 
into two groups:
* Linear data structure 
* Non-linear data structure

#### Linear data structure
Linear data structure is a sequential type of data structure, that means that all the elements in 
the memory are stored in one element after the other. There are different linear data structures which
hold sequential values such as: 
* Array
* Linked list
* Stack
* Queue

#### Non-linear data structure
It is a form of data structure where the data elements don’t stay arranged in a contiguous manner. 
Since these data structures are non-linear, they involve a multiple levels. The non-linear data 
structures are: 
* Tree
* Graph

### Data Structure Basic Operations
As data structures are techniques of storing and organizing the data in such a way that the data can 
be utilized in an efficient manner. The data in the data structures are processed by certain 
operations. The particular data structure we chose largely depends on the frequency of the operation 
that needs to be performed on the data structure.

The basic data structure operations are:
* Traversing: Refers to the process of visiting each node in a data structure.
* Searching: Is the process of finding a given value position in a collection of values.
* Insertion: Add one or more data elements into a data structure at a given value position.
* Deletion: Remove an existing element from a data structure at a given position and re-organizing 
all elements.
* Sorting: Refers to changing the value of an existing element of a data structure at a given position.

### Arrays
Arrays are defined as the collection of items with same data types stored at contiguous memory locations.
Each item stored in an array is called an element. Each location of an element in an array has a numerical
value which is used to identify the element, and we call it index. Each data element in an Array can be 
randomly accessed by using its index number.

Arrays are useful because:
* Searching a value in an array is easier.
* Arrays are good for storing multiple values.
* Arrays are best to process multiple values quickly and easily.

Following are the basic operations supported by an array:
* Access − Reads the value of an element in the array with constant time O(1) knowing its index.
* Search − Searches an element using the given value with linear time complexity O(n).
* Insertion − Adds an element at the given position with runtime complexity O(n).
* Deletion − Deletes an element at the given index and time complexity O(n).

In array, space complexity for worst case is O(n), where 'n' is the number of elements in the given array.

#### Advantages of Array
- Array provides the single name for the group of variables of the same data type. 
- Traversing an array is a very simple process; we just need to increment the base address of the array 
in order to visit each element one by one.
- Any element in the array can be directly accessed by using the index.

#### Disadvantages of Array
- Array is homogenous, it means that only elements with similar data type can be stored in it.
- In array, there is static memory allocation that is size of an array cannot be altered.
- There will be wastage of memory if we store lesser number of elements than the declared size.
- If a smaller array is used, we should have to copy the values in a larger array.

### Linked Lists
Linked list is a linear data structure that includes a series of connected nodes. Linked list can be 
defined as nodes that are randomly stored in the memory but connected to each other. A node in the 
linked list contains two pieces of data, first is the value and second is the address of the *next* node 
in the list. The first node in a Linked list is known as the *head*, the last node of the list, the 
*tail*, contains a pointer to a null value.

Linked list is a data structure that overcomes the limitations of arrays. 

Linked list is useful because:
* It allocates the memory dynamically. All the nodes of the linked list are non-contiguously stored in 
the memory and linked together with the help of pointers.
* In linked list, size is no longer a problem since we do not need to define its size at the time of 
declaration. List grows as per the program's demand and limited to the available memory space.

#### Operations performed on Linked list
The basic operations that are supported by a list are mentioned as follows:
* Insertion - This operation is performed to add an element into the list. Time complexity O(1).
* Deletion - It is performed to delete an operation from the list. Time complexity O(1).
* Access - It is performed to access the value of an elements in the list using the given key. Time 
complexity O(n).
* Search - It is performed to search an element from the list by its value. Time complexity O(n).

#### Advantages of Linked list
* Dynamic data structure - The size of the linked list may vary according to the requirements. Linked list 
does not have a fixed size.
* Insertion and deletion - Unlike arrays, insertion, and deletion in linked list is easier.
* Memory efficient - The size of a linked list can grow or shrink according to the requirements, so memory 
  consumption in linked list is efficient.
* Implementation - We can implement both stacks and queues using linked list.

#### Disadvantages of Linked list
* Memory usage - In linked list, node occupies more memory than array. Each node of the linked list 
occupies two types of variables, one is a data variable, and another one is the pointer variable.
* Traversal - Traversal is not easy in the linked list. If we have to access an element in the linked list, 
  we cannot access it randomly, while in case of array we can randomly access it by index. 
* Reverse traversing - Backtracking or reverse traversing is difficult in a linked list.

### Stacks

### Queues

### Strings

### Sets

### Maps

### Hash Tables

### Graphs

### Trees

### Heaps

## Algorithms

Correctness

Efficiency: Time Complexity, Space Complexity

### Search

### Sort

### Insert

### Update

### Delete

### Graph Traversal

### Tree Traversal

### Dynamic Programming

### Hashing