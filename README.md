# Easy to Advanced Data Structures Notes and Code
This repository contains notes and code implementing everything I have learned from "Easy to Advanced Data Structures" a free online course on Udemy/Youtube by William Fiset.

* https://www.udemy.com/course/introduction-to-data-structures/
* https://www.youtube.com/watch?v=Qmt0QwzEmh0&list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu

## Overview
* Static and dynamic arrays
* Singly and doubly linked lists
* Stacks
* Queues
* Heaps/Priority Queues
* Binary Trees/Binary Search Trees
* Union find/Disjoint Set
* Hash tables
* Fenwick trees
* AVL trees
* Binary Indexed trees
* Sparse tables

## Singly and doubly linked lists

The linked list data structures consist of a sequential list of nodes that hold data. Depending if the linked list is singly or doubly linked each node will point to one or two other nodes respectively. There are several key nodes in a linked list
* Head Node
  * Is the entry point of the linked list most traverseal of a linked list will begin here
* Current Node/ Traverse Point
  * Are markers used to traverses a linked list and perform operation such as inserting and removing nodes
* Tail
  * Is the the last node in a linked list, it can be kept track of for fast insertion at the end of a linked list or as a 2nd entry point into a doubly linked list.
  
See _Figure 1: Singly link list Diagram_ for an illustration of a singly linked list with all of its components.


<p align="center">
  <img src="https://github.com/Melvin-Cordon/Easy-to-Advanced-Data-Structures/blob/master/Images/LinkedListDiagram.png">
</p>

<p align="center">
  Figure 1: Singly link list Diagram
</p>

### Inserting at the beginning of a linked list:
1. Create a New Node then assign it to "Current Node"
2. Assign the "Head Node" to the point "Next" of the "Current Node" 
3. Make the "Current Node" the "Head Node"

See _Figuer 2: Inserting a node at the beginning of a linked list_ for an illustration of how inserting a node at the beginning of linked list.



<p align="center">
  <img src="https://github.com/Melvin-Cordon/Easy-to-Advanced-Data-Structures/blob/master/Images/LinkedListDiagram_insert_beginning.png">
</p>

<p align="center">
  Figuer 2: Inserting a node at the beginning of a linked list
</p>
