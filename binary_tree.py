# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 09:15:28 2019

@author: HARSH
"""

class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
        
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
            
    def insertTree(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insertTree(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insertTree(data)
        else:
            self.data = data
            
    def searchTree(self, val):
        if val < self.data:
            if self.left is None:
                return 'Not found'
            return self.left.searchTree(val)
            
        elif val > self.data:
            if self.right is None:
                return 'Not found'
            return self.right.searchTree(val)
        else:
            return str(self.data) + ' is found'
            
            
root = Node(12)
root.insertTree(6)
root.insertTree(14)
root.insertTree(3)
root.printTree()

print(root.searchTree(3))
print(root.searchTree(22))