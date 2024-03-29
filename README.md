# Data Structure and Algorithms
Data Structures and Algorithms concepts and implementation using python

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

Time complexity in computer terms indicates the runtime an algorithm require to complete a
certain task. On the oder hand, space complexity refers to amount memory required by such algorithm.

Common values of algorithm complexity are, starting from the most efficient:
* **O(1):** Constant
* **O(log n):** Logarithmic
* **O(n):** Linear
* **O(n log n):** Quasi-linear
* **O(n^2):** Quadratic
* **O(2^n):** Exponential
* **O(n!):** Factorial

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
* **Integers:** The integer data type contains whole numbers that can be either negative or positive 
numeric values.
* **Floating:** The float is a data type that can hold decimal values.
* **Boolean:** It is a data type that can hold either a `True` or a `False` value.
* **Character:** It is a data type that can hold a single character value both uppercase and lowercase.

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
* **Traversing:** Refers to the process of visiting each node in a data structure.
* **Searching:** Is the process of finding a given value position in a collection of values.
* **Insertion:** Add one or more data elements into a data structure at a given value position.
* **Deletion:** Remove an existing element from a data structure at a given position and re-organizing 
all elements.
* **Sorting:** Refers to changing the value of an existing element of a data structure at a given position.

### Arrays
Arrays are defined as the collection of items with same data types stored at contiguous memory locations.
Each item stored in an array is called an *element*. Each location of an element in an array has a 
numerical value which is used to identify the element, and we call it *index*. Each data element in an 
Array can be randomly accessed by using its index number fast. However, adding or inserting new data at a
specific location in an Array carries high costs.

Arrays are useful because:
* Searching a value in an array is easier.
* Arrays are good for storing multiple values.
* Arrays are best to process multiple values quickly and easily.

#### Arrays Basic Operations
Following are the basic operations supported by an array:
* Access − Reads the value of an element in the array with constant time `O(1)` knowing its index.
* Search − Searches an element using the given value with linear time complexity `O(n)`.
* Insertion − Adds an element at the given position with runtime complexity `O(n)`.
* Deletion − Deletes an element at the given index and time complexity `O(n)`.

In array, space complexity for worst case is `O(n)`, where `n` is the number of elements in the given 
array.

#### Advantages of Array
- Array provides the single name for the group of variables of the same data type. 
- Traversing an array is a very simple process; we just need to increment the base address of the array in 
  order to visit each element one by one.
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
* **Insertion** - This operation is performed to add an element into the list. Time complexity `O(1)`.
* **Deletion** - It is performed to delete an operation from the list. Time complexity `O(1)`.
* **Access** - It is performed to access the value of an elements in the list using the given key. Time 
complexity `O(n)`.
* **Search** - It is performed to search an element from the list by its value. Time complexity `O(n)`.

#### Advantages of Linked list
* **Dynamic data structure** - The size of the linked list may vary according to the requirements. Linked 
list does not have a fixed size.
* **Insertion and deletion** - Unlike arrays, insertion, and deletion in linked list is easier.
* **Memory efficient** - The size of a linked list can grow or shrink according to the requirements, so 
memory consumption in linked list is efficient.
* **Implementation** - We can implement both stacks and queues using linked list.

#### Disadvantages of Linked list
* **Memory usage** - In linked list, node occupies more memory than array. Each node of the linked list 
occupies two types of variables, one is a data variable, and another one is the pointer variable.
* **Traversal** - Traversal is not easy in the linked list. If we have to access an element in the linked 
list, we cannot access it randomly, while in case of array we can randomly access it by index. 
* **Reverse traversing** - Backtracking or reverse traversing is difficult in a linked list.

### Stacks
A stack is an Abstract Data Type that allows operations at one end only. At any given time, we can only 
access the top element of a stack. This means, Stack is a special linear data structure that follows 
the Last-In-First-Out (LIFO) principle. 

In stack terminology, insertion operation is called *push* and removal operation is called *pop*. 
A pointer called *top* is used to keep track of the top element in the stack.

Although stack is a simple data structure to implement, it is very powerful. Stacks are useful because:
* Stack is used for performing UNDO/REDO operation. 
* Recursion, it means a function which calls itself, to maintain all the previous records of the function, 
the compiler creates a system stack. 
* Depth First Search is implemented on Graphs uses the stack data structure. 
* Computer memory management; the stack manages the memory. When the function is created, all its 
variables are assigned in the stack memory. When the function completed its execution, all the variables 
assigned in the stack are released.

#### Stacks Basic Operations 
Stacks normally support tow basic operations:
* **Push** - Insert (store) a new element to the top of a stack.
* **Pop** - Remove (access) an element from the top of a stack.

To use a stack efficiently, we need to check the status of stack as well. For the same purpose, the 
following functionality is added to the stacks:
* **Is Empty** - Check if the stack is empty.
* **Is Full** - Check if the stack is full.
* **Peek** - Get the value of the front element without removing it.

Stack Time Complexity depends on the base implementation. For the array-based implementation of a stack, 
the push and pop operations take constant time `O(1)`. On the other hand, when a Linked list is used to
implement a Stack, the time complexity for the push operation is constant `O(1)`, but popping the
last element has a linear time complexity `O(n)`.

### Queues
Queue is an abstract data structure that is open at both ends, rear and front. One end is always used 
to insert data and the other is used to remove data. Queue follows First-In-First-Out (FIFO) principle.

Queues maintain two data pointers, *front* points to the element at the head of the queue and *rear* points
to the tail item. Putting items in the queue is called *enqueue*, and removing items from the queue is 
called *dequeue*.

Due to the fact that queue performs actions on first in first out basis which is quite fair for the 
ordering of actions. Queues are useful because:
* Queues are widely used as waiting lists for a single shared resource like printer, disk, CPU.
* Queues are used in asynchronous transfer of data.
* Queues are used as buffers in many multimedia applications. 
* Queues are used in operating systems for handling interrupts.
* Queues are used inDepth First Search is implemented on Graphs data structure.

#### Queue Basic Operations 
Here are the basic operations associated with queues :
* **Enqueue** - Add (store) a new item to the tail of a queue.
* **Dequeue** - Remove (access) an item from the head of a queue.

Other functions are required to make the fundamental queue operations more efficient:
* **Peek** - Get the value of the top item without removing it.
* **Is Empty** - Check if the queue is empty.
* **Is Full** - Check if the queue is full.

Queue Time Complexity depends on the base implementation. For the array-based implementation of a queue, 
the enqueue and dequeue operations take constant time `O(1)` to write and remove values on the base array. 
Despite they array-based fast operations, Linked list implementations are preferred, because of the 
scalability and memory issues with arrays.

When a Linked list is used to implement a queue, the time complexity for the enqueue and dequeue operation 
are constant `O(1)`. Even though, the space complexity of linked representation of a queue with `n` 
elements is `O(n)`.

### Strings
Strings are not a data structure, they are a data type. But strings are a data type that are stored in data 
structure. Strings are defined as an array of characters. The difference between a character array and a 
string is the string is terminated with a special character `\0`. 

`\0` represents the end of the string. It is also referred as String terminator or Null Character. 
Normally, strings are surrounded double quotation marks.

As strings are collection of characters, therefore they have length to indicate the size of the string. 
Strings also have indexes to indicate the location of each character, so that we could easily find out 
some character. The index of the position start with 0 as in the array data structure. We could get access 
to any character by using a bracket and the index of the position.

As number are part of the char set, numbers can also be expressed as strings. However, Strings can not be 
used in the mathematical operations. In some languages strings are represented as primitive data types and 
others as class of immutable objects.

### Hash Tables
A Hash Table is an abstract data structure which stores data in an associative manner. Hash Table maps 
keys to value and uses a hash function to compute an index, into an array of buckets, from which the 
desired value can be stored or retrieved. Hash tables are the most frequently used implementation of 
a Map or Dictionary data type, in this case is with an array combined with a hash function.

Following are the basic primary operations of a hash table:
* **Search** − Searches an element in a hash table.
* **Insert** − Inserts an element in a hash table.
* **Delete** − Deletes an element from a hash table.

Hash Table provides constant time `O(1)` for searching, insertion and deletion operations on average. 
Contrary, Hash Tables collisions are practically not be avoided for large set of possible keys. Hash Tables 
are inefficient when there are many collisions.

Hash tables are implemented where
* Constant time lookup and insertion is required
* Associative arrays
* Cryptographic applications
* Database indexing
* Hash tables can be used in the implementation of Set data structure

In a hash table, data is stored in an array format, where each data value has its own unique index value. 
Access of data becomes very fast if we know the index of the desired data. To understand better a Hash Table
we need to know first what hashing is.

#### Hash Function
Hashing is a technique to generate an integer value from a given key. A Hash function `h` maps a unique 
index with an arbitrary value. Using the hash function, we can calculate at constant time the address at 
which the value can be stored in an Array.

The main idea behind the hashing is to create the (key/value) pairs. If the key is given, then the algorithm 
computes the index at which the value would be stored. It can be written as `index = hash(key)`. So, a Hash
function takes a key, convert it to some sort of integers and then, remaps that hash code to an index.

A good hash function may not prevent the collisions completely however it can reduce the number of 
collisions. A has function should always produce the same result when passing the same input. A hash function
need to be fast. The hash function result should be as much random as possible.

A Hashtable has two main parameters that may affect its performance, initial capacity and load factor. The 
*capacity* `M` is the number of buckets in the hash table, and the initial capacity is simply the capacity 
at the time the hash table is created. The *load factor* `a` is a measure of how full the hash table is 
allowed to get before its capacity is automatically increased. Load factor `a = n/M`, where `n` is the 
number of entries occupied in the hash table.

There are several algorithms for hashing integers indexes from a given key. The most common methods are:
* **Division method** - A standard technique is to use a modulo function on the key, by selecting a divisor 
`M` which is a prime number close to the table size, so `h(k) = k Mod M`.
* **Folding method** - A folding hash code is produced by dividing the input into n sections of m bits, 
where 2^m is the table size.
* **Mid-square method** - A mid-squares hash code is produced by squaring the input and extracting an 
appropriate number of middle digits or bits.
* **Multiplication method** - Standard multiplicative hashing uses the formula `h(k) = floor(m (k A Mod 1))`.

A perfect hash function is one that maps each different key to a distinct integer to the table such that 
no two search keys hashes to the same array index.

#### Collision
A hash collision is when the hash function generates the same index for multiple keys. This produce a 
conflict on what value to be stored in that index. While the goal of a hash function is to minimize 
collisions, some collisions are unavoidable in practice. The second part of the hashing algorithm is 
collision resolution.

To resolve hashing collisions we can use one of the following techniques:
* **Closed Addressing:** A key is always stored in the bucket it's hashed to. Collisions are dealt with 
  using separate data structures on a per-bucket basis. It stores arbitrary number of keys per bucket. It 
  is also known as Open Hashing.
* **Open Addressing:** With this method a hash collision is resolved by probing, or searching through 
  alternative locations in the array until the target record is found. At most, it stores one key per 
  bucket. It is also known as Closed Hashing.

#### Closed Addressing
Separate chaining using Linked lists is the common closed addressing collision resolution method. In 
separate chaining, the process involves building a linked list with key–value pair for each search array 
index. The collided items are chained together through a single linked list, which can be traversed to 
access the item with a unique search key. 

#### Open Addressing
In Open Addressing every entry records are stored in the bucket array itself, and the hash resolution is 
performed through probing. When a new entry has to be inserted, the buckets are examined, starting with 
the hashed-to slot and proceeding in some probe sequence, until an unoccupied slot is found. When searching 
for an entry, the buckets are scanned in the same sequence, until either the target record is found, or an 
unused array slot is found.

Different techniques used in open addressing are:
* Linear probing, in which the interval between probes is fixed (usually 1).
* Quadratic probing, in which the interval between probes is increased by adding the successive outputs of 
  a quadratic polynomial to the value given by the original hash computation.
* Double hashing, in which the interval between probes is computed by a secondary hash function.

### Trees
A tree data structure is defined as a collection of objects or entities known as *nodes* that are linked 
together to represent hierarchy. Trees are a non-linear data structure because they do not store data in a 
sequential manner. They are hierarchical structures because the elements in a Tree are arranged in multiple 
levels.

In the Tree data structure, the topmost node is known as a *root node*. Each node contains some data and 
the link or reference of other nodes, they are called *children*. The connecting links between nodes
is called *edges*. Endpoints that have no children nodes are known as ‘leaf’ nodes.

Each node in the tree can be connected to many children (depending on the type of tree), but must be 
connected to only one *parent*, except for the root node, which has no parent. Based on these constraints, 
no node can be its own ancestor. But, also each child can be treated like the root node of its own subtree, 
making recursion a useful technique for working on trees.

The following are common applications of tree data structures:
- Trees are used to store the data in the hierarchical structure. For example, the file system.
- It is used to implement other data structures as the Heaps.
- Most popular databases use different variants of the tree structure to store and indexing their data.
- The tree data structure is also used to store the data in routing tables in the routers.

#### Trees Basic Operations 
The basic operations that can be performed on a binary search tree data structure, are the following:

* *Insert* − Inserts an element in a tree/create a tree.
* *Delete* − Removes an element from a tree/delete a tree.
* *Search* − Searches an element in a tree.
* *Preorder Traversal* − Traverses a tree in a pre-order manner.
* *Inorder Traversal* − Traverses a tree in an in-order manner.
* *Postorder Traversal* − Traverses a tree in a post-order manner.

#### Advantages of Trees
The Tree data structures allow quicker and easier access to the data as it is a non-linear data structure. 
This allows for a faster response time during a search as well as greater convenience during the design 
process. Other data structures such as arrays, linked list, stack, and queue are linear data structures 
that store data sequentially. In order to perform any operation in a linear data structure, the time 
complexity increases with the increase in the data size. 

#### Types of Trees
A *General Tree* is characterised by the lack of any configuration or limitations on the number of children 
a node can have. Any tree with a hierarchical structure can be described as a general tree. A node can 
have any number of children, and the tree’s orientation can be any combination of these. The degree of the 
nodes can range from 0 to n.

##### Binary Tree
A Binary Tree is a tree data structure in which each parent node can have at most two children. Each node 
of a Binary Tree consists of three items: 
- Data item
- Address of left child
- Address of right child

*Binary trees* are a commonly used type and when the order of the children is specified, this data structure 
corresponds to an ordered tree in graph theory. 

In addition, there are son special types of Binary Tree as:
- Full Binary Tree
- Perfect Binary Tree
- Complete Binary Tree
- Balanced Binary Tree

##### Binary Search Tree
A Binary Search Tree follows specific order to arrange the elements.  Binary Search Tree (BST) is a 
subtype of binary tree that is organised in such a way that it allows for faster searching, lookup, and 
addition/removal of data. It is called a Binary Tree because each tree node has a maximum of two children.
And it is called a Search Tree because of its properties to search for a value in order of `O(log n)` time.

A Binary Search Tree is governed by the following arrangement rules:
1. All nodes of left subtree are less than the root node.
2. All nodes of right subtree are more than the root node.
3. Both subtrees of each node are also BSTs, they fulfill the above two properties.

##### AVL Tree
The Adelson-Velsky-Landis (AVL) Tree can be defined as height balanced binary search tree in which each 
node is associated with a *balance factor* which is calculated by subtracting the *height* of its right 
subtree from that of its left subtree. AVL Tree checks the height of the left and the right subtrees and 
assures that the difference is not more than 1. This difference is called the balance factor.

As Binary Search Tree worst-case performance is closest to linear search algorithms, that is `Ο(n)`. In 
real-time applications, we cannot predict data pattern and their frequencies. So, a need arises to balance 
out the existing BST. 

To balance itself, an AVL Tree may perform the following four kinds of operations:
- Left rotation 
- Right rotation
- Left-Right rotation
- Right-Left rotation

##### B Tree
B-tree is a special type of self-balancing search tree in which each node can contain more than one key 
and can have more than two children. It is a generalized form of the binary search tree. It is also a 
height-balanced m-way tree. 

B-Tree is a data structures that sorts data in logarithmic time to allow for search, sequential access, 
deletions, and insertions. A B-tree, unlike a binary tree, allows its nodes to have more than two children. 
They can read and write larger blocks of data in databases and file systems.

A B-tree should contain the following properties:
1. For each node `x`, the keys are stored in increasing order.
2. In each node, there is a boolean value `x.isLeaf` which is true if `x` is a leaf.
3. If `n` is the order of the tree, each internal node can contain at most `n - 1` keys along with a pointer 
   to each child. 
4. Each node except root can have at most n children and at least `n/2` children.
5. All leaves have the same depth (i.e. height-h of the tree).
6. The root has at least 2 children and contains a minimum of 1 key.
7. If `n ≥ 1`, then for any n-key B-tree of height h and minimum degree `t ≥ 2`, `h ≥ log t (n+1)/2`.

### Graphs
A graph is a non-linear data structure that contains *vertices* and *edges*. A graph `G` is defined as a 
collection of vertices and edges `G = {V, E}`, where `V` is the set of vertices (nodes) and `E` is the set 
of edges that are used to connect these vertices. A graph can be seen as a cyclic tree, where the vertices 
maintain any complex relationship among them, instead of having parent child relationship.  

 Each node of the graph is represented as a vertex. In a Graph a vertex is said to be *adjacent* to another 
 vertex if there is an edge connecting them. Edge represents a *path* between two vertices or a line between 
 two vertices. Path represents a sequence of edges between the two vertices.

A graph can be directed or undirected. In a directed graph, edges form an ordered pair. Edges represent a 
specific path from some **vertex A** to another **vertex B**. Node **A** is called initial node while node 
**B** is called terminal node. However, in an undirected graph, edges are not associated with the 
directions with them. An undirected graph if an edge exists between vertex **A** and **B** then the vertices 
can be traversed from **B** to **A** as well as **A** to **B**. 

#### Common Applications of Graph:
- Graphs are used to represent flow of control in computers.
- Graphs are used in many social networking sites.
- Graphs are used in maps applications to find the shortest route to a destination.
- Graphs are also used in airlines system for effective route optimization. 
- In transportation, graphs are used to find the shortest path.
- In circuits, graphs can be used to represent electric components as nodes and wires as edges.
- Graphs are used in computer networks for Peer to Peer (P2P) applications.

#### Graphs Basic Operations 
The most common graph operations are:
* Graph Traversal - Visiting all the nodes of a graph.
* Add - Add elements(vertex or edges) to the graph.
* Remove - Remove elements(vertex or edges) from the graph.
* Get - Returns the element associated with a value in the graph.
* Path - Finding the path from one vertex to another.

#### Advantages of Graph:
- By using graphs we can easily find the shortest path, neighbors of the nodes, and many more.
- Graphs are used to implement algorithms like Depth First Search (DFS) and Breadth First Search (BFS). 
- It is used to find minimum spanning tree which has many practical applications.
- It helps in organizing data.
- As a non-linear structure, Graphs help in understanding complex problems and their visualization.

#### Disadvantages of Graph:
- Graphs use lots of pointers which can be complex to handle.
- It can have large memory complexity.

### Sets
A set is a data structure that can store any number of unique values without any particular order. Set’s 
differ from arrays in the sense that they only allow non-repeated, unique values within them. Sets are a 
computer implementation of the mathematical concept of a finite Set. 

Sets can be implemented using various data structures, which provide different time and space trade-offs 
for various operations. A simple implementation is to use a list, ignoring the order of the elements and 
taking care to avoid repeated values. This is simple but inefficient, as operations like set membership or 
element deletion are `O(n)`, as they require scanning the entire list. Sets are often instead implemented 
using more efficient data structures, like various flavors of trees, tries, or hash tables.  

As sets can be interpreted as a kind of map. These are commonly implemented in the same way as partial maps 
(associative arrays), in this case in which the value of each key-value pair use the same value. This 
implementation with hash table offers a `O(1)` time complexity on average-case, but `O(n)` worst-case, for 
most operations on unsorted sets. The self-balancing binary search tree implementation for set sorted sets 
has `O(log n)` for most operations.

#### Set Basic Operations 
One may define the operations of the algebra of sets as:
* Union(S,T): returns the union of sets S and T.
* Intersection(S,T): returns the intersection of sets S and T.
* Difference(S,T): returns the difference of sets S and T.
* Subset(S,T): a predicate that tests whether the set S is a subset of set T.
* pick(S): returns an arbitrary element of S.
* pop(S): returns an arbitrary element of S, deleting it from S.
* add(S,x): adds the element x to S, if it is not present already.
* remove(S, x): removes the element x from S, if it is present.

#### Advantages of Set:
* Set can be used to store unique values in order to avoid duplications of elements present in the set.
* Elements in a set are stored in a sorted fashion which makes it efficient.
* Set are dynamic, so there is no error of overflowing of the set.
* Searching operation takes O(logN) time complexity.

Realtime Applications of Set:
- Set are used in the music player app to list all the songs in proper order.
- Set are used to determine the distinct values in an array.
- Set are used to detect cycles in a Linked List.
- Sets are used in various database operations such as performing.

### Tries
Trie is a tree-based data-structure that stores the set of strings in a sorted way. It has the number of 
pointers equal to the number of characters of the alphabet in each node. It can search a word in the 
dictionary with the help of the word's prefix. Assuming that all strings are formed from the letters 'a' 
to 'z' in the English alphabet, each trie node can have a maximum of 26 points. The word "Trie" is an 
excerpt from the word "retrieval". 

Tries are sometimes Space-Efficient. If you're storing lots of words that start with similar patterns, tries 
may reduce the overall storage cost by storing shared prefixes once. Efficient Prefix Queries. Tries can 
quickly answer queries about words with shared prefixes, like: How many words start with "choco"?
What's the most likely next letter in a word that starts with "strawber"? It provides an alphabetical 
filter of entries by the key of the node. 

Properties of the Trie for a set of the string:
- The root node of the trie always represents the null node.
- Each child of nodes is sorted alphabetically.
- Each node can have a maximum of 26 children (A to Z).
- Each node (except the root) can store one letter of the alphabet.

Common applications of Trie data structure include: 
* Spell Checker. Trie is used to store the word in dictionaries. The spell checker can easily be applied 
  in the most efficient way by searching for words on a data structure. 
* Auto-complete. It provides a simple way to find an alternative word to complete the word for the 
  following reasons. 
* Browser history. It is also used to complete the URL in the browser.

#### Tries Basic Operations 
* Insert
* Search
* Delete

### Heaps
Heap is a special case of balanced binary tree data structure where the root-node key is compared with its 
children and arranged accordingly. A heap is a **complete binary tree**, and the binary tree is a tree in 
which the node can have utmost two children. A complete binary tree is a binary tree in which all the 
levels except the last level, i.e., leaf node should be completely filled, and all the nodes should be 
left-justified. 

Heap data structure must satisfy the heap property, where any given node is
- Always greater than its child node/s and the key of the root node is the largest among all other nodes. 
  This property is also called max heap.
- Always smaller than the child node/s and the key of the root node is the smallest among all other nodes. 
  This property is also called min heap.

The total number of comparisons required in the max heap is according to the height of the tree. The 
height of the complete binary tree is always `log n`; therefore, the time complexity would also be `O(log 
n)`. The heap is one maximally efficient implementation of an abstract data type called a priority queue.

#### Heap Basic Operations
* **Insert** - Insert Element into Heap.
* **Delete** - Delete Element from Heap.
* **Peek** - Peek operation returns the maximum element from Max Heap or minimum element from Min Heap.
* **Extract** - Extract-Max returns the node with maximum value after removing it from a Max Heap whereas 
  Extract-Min returns the node with minimum after removing it from Min Heap. 

The heap data structure has many applications.
- Heapsort: One of the best sorting methods being in-place and with no quadratic worst-case scenarios.
- Selection algorithms: A heap allows access to the min or max element in constant time, and other 
  selections (such as median or kth-element) can be done in sublinear time on data that is in a heap
- Priority Queue: A priority queue is an abstract concept like "a list" and can be implemented with a heap.
- 
## Algorithms
An algorithm is a set of well-defined instructions to solve a particular problem. It takes a set of inputs 
and produces the desired output.  The formal definition of an algorithm is that it contains the finite set 
of instructions which are being carried in a specific order to perform the specific task. 

The following are the characteristics of an algorithm:
* Input: An algorithm has some input values. We can pass 0 or some input value to an algorithm.
* Output: We will get 1 or more output at the end of an algorithm.
* Unambiguity: An algorithm should be unambiguous which means that the instructions in an algorithm should 
  be clear and simple.
* Finiteness: An algorithm should have finiteness. Here, finiteness means that the algorithm should contain 
  a limited number of instructions, i.e., the instructions should be countable.
* Effectiveness: An algorithm should be effective as each instruction in an algorithm affects the overall 
  process.
* Language independent: An algorithm must be language-independent so that the instructions in an algorithm 
  can be implemented in any of the languages with the same output.

Correctness

Efficiency: Time Complexity, refers to the relationship between the growth of input size of an algorithm and 
the growth of the operations executed.

Space Complexity

## Algorithms

### Search

#### Linear Search

#### Binary Search

### Sort

#### Selection Sort

#### Bubble Sort

#### Insertion Sort

#### Merge Sort

#### Quick Sort

### Insert

### Update

### Delete

### Recursion

### Top K element

### Backtracking

### Sliding Window

### Tree Traversal

### Graph Traversal

#### Depth First Search

#### Breadth First Search

### Dynamic Programming

### Topological Sorting

### Dijkstra's Algorithm

### Greedy Algorithm

### Intervals

### Math Algorithms

### Bit Manipulation
