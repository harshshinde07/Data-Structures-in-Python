# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 14:47:01 2019

@author: HARSH
"""

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None
        
class DoubleLinkedList:
    def __init(self):
        self.head = None
        
    def printList(self):
        val = self.head
        while val.next is not None:
            print(val.data)
            val = val.next
        print(val.data)
    
    def insertBeginning(self, data):
        node = Node(data)
        node.prev = None
        node.next = self.head
        self.head = node
    
    def insertMiddle(self, middle, data):
        if middle is None:
            print('Node not found')
        val = Node(data)
        val.next = middle.next
        val.prev = middle
        middle.next = val
    
    def insertEnd(self, data):
        val = Node(data)
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = val
        val.next = None
        val.prev = curr
    
    def removeVal(self, data):
        curr = self.head
        while curr.next is not data:
            curr = curr.next
        curr.next = data.next
    
linkedList = DoubleLinkedList()
linkedList.head = Node('First')
second = Node('Second')
third = Node('Third')
linkedList.head.next = second
second.next = third

linkedList.insertBeginning('Zeroth')
linkedList.insertEnd('Last')
linkedList.insertMiddle(second, 'Middle')
linkedList.printList()
linkedList.removeVal(third)
linkedList.printList()