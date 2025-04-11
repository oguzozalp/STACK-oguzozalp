# ds.py

class Node:
    def __init__(self, data):
        self.data = data


class LinkedListNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, node, index):
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            prev = self.head
            for _ in range(index - 1):
                if prev is None:
                    raise IndexError("Index out of range")
                prev = prev.next
            node.next = prev.next
            prev.next = node

    def remove_node(self, index):
        if self.head is None:
            raise IndexError("List is empty")
        if index == 0:
            removed = self.head
            self.head = self.head.next
            return removed
        prev = self.head
        for _ in range(index - 1):
            if prev.next is None:
                raise IndexError("Index out of range")
            prev = prev.next
        removed = prev.next
        prev.next = removed.next
        return removed


class Stack:
    def __init__(self):
        self.list = LinkedList()

    def push(self, node):
        self.list.add_node(node, 0)

    def pop(self):
        return self.list.remove_node(0)

    def peek(self):
        if self.list.head is None:
            return None
        return self.list.head
