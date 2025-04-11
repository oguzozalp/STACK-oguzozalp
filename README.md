##  OĞUZ BARAN ÖZALP - 2200674049



# STACK Project

## Overview

I created this project as a personal learning exercise to dive into data structures and object-oriented programming using Python. In this project, I implemented a linked list-based stack in the `ds.py` file and demonstrated its functionality in the `main_LL.py` script. Additionally, I included a CSV file with coordinate data as a sample dataset to potentially integrate with the project in future enhancements.

## Files

### ds.py
In this file, I defined a set of classes that form the backbone of the data structures in this project:
- **Node:** A base class that simply holds a data element.
- **LinkedListNode:** An extension of the base Node that introduces a pointer to the next node.
- **LinkedList:** A custom linked list implementation that allows me to add or remove nodes at any index. I designed this to serve as the underlying structure for more complex data structures.
- **Stack:** I built the stack data structure on top of my linked list by always adding new elements to the beginning. This design choice ensures that the most recently pushed element is always at the top, enabling efficient push, pop, and peek operations.

### main_LL.py
This script is my demonstration and testing ground for the stack implementation:
- I create an instance of the `Stack` class.
- I push several nodes onto the stack, each holding an integer value.
- I display the top element using the `peek()` method.
- I perform a `pop()` operation to remove the top element and print its value.
- Finally, I verify that the subsequent element moves to the top of the stack after popping.

### coordinates.csv
This CSV file contains sample data with the following columns: id, latitude, longitude, and name. The file lists details such as:
- **A:** Geomatics Engineering (Latitude: 39.865547, Longitude: 32.733881)
- **B:** Library (Latitude: 39.870883, Longitude: 32.734847)
- **C:** Refectory (Latitude: 39.867947, Longitude: 32.737289)

I plan to use this data for future extensions of the project—for instance, to map these coordinates or to integrate data-driven features within the project.

## Implementation Details

In developing the data structures, I focused on:
- **Simplicity and Clarity:** I aimed for my code to be easy to understand and modify. Each class in `ds.py` is modular, allowing me to expand or replace parts of the functionality with ease.
- **Practical Application:** The stack, implemented in a linked list format, mimics real-world stack behavior where the last pushed item is the first to be removed (LIFO principle).
- **Error Handling:** In my linked list operations, I’ve introduced basic error checking (such as ensuring indices are within bounds) to prevent runtime errors during node manipulation.

## Motivation

I built this project to deepen my understanding of how data structures work at a fundamental level. By implementing a stack using a linked list, I learned a lot about memory management and pointer operations in Python. Moreover, this project serves as a stepping stone for experimenting with more complex data algorithms and structures in the future.

## How to Run the Project

To run this project on your local machine, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/oguzozalp/STACK-oguzozalp.git
