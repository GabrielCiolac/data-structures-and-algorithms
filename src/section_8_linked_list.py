#!/usr/bin/env python3

from typing import Any, Optional


class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data=None) -> None:
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node
        self.length += 1

    def prepend(self, data=None) -> None:
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        node.next = self.head
        self.head = node
        self.length += 1

    def get_index(self, index:int) -> Optional[Any]:
        node = self.head
        for i in range(index):
            if node is None:
                return None
            node = node.next
        return node.value
    
    def insert(self, index:int, data=None) -> None:
        if index == 0:
            self.prepend(data)
            return
        if index == self.length:
            self.append(data)
            return
        node = Node(data)
        prev = self.head
        for i in range(index - 1):
            prev = prev.next
        node.next = prev.next
        prev.next = node
        self.length += 1

    def remove(self, index:int) -> None:
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        prev = self.head
        for i in range(index - 1):
            prev = prev.next
        prev.next = prev.next.next
        self.length -= 1

    def reverse(self) -> 'LinkedList':
        new_list = LinkedList()
        node = self.head
        while node is not None:
            new_list.prepend(node.data)
            node = node.next
        return new_list
    
    def list_to_linked_list(self, input_list:list) -> 'LinkedList':
        new_list = LinkedList()
        for item in input_list:
            new_list.append(item)
        return new_list

    def __len__(self) -> int:
        return self.length
    
