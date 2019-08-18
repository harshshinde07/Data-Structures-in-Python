# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Single linked list 

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        
class SingleLinkedList:
    def __init__(self):
        self.head = None
        
    def printList(self):
        val = self.head
        while val.next is not None:
            print(val.data)
            val = val.next
        print(val.data)
        
    def insertBeginning(self, data):
        val = Node(data)
        val.next = self.head
        self.head = val
        
    def insertEnd(self, data):
        val = Node(data)
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = val
        val.next = None
        
    def insertMiddle(self, middle, data):
        if middle is None:
            print('Node is not found')
            return
        val = Node(data)
        val.next = middle.next
        middle.next = val
        
    def removeVal(self, node):
        val = self.head
        while val.next is not node:
            val = val.next
        #temp = val.next
        val.next = node.next       
            
    
linkedList = SingleLinkedList()
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
            
