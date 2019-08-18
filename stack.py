# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 09:06:45 2019

@author: HARSH
"""

class Stack:
    
    def __init__(self):
        self.stack = []
        
    def peek(self):
        return self.stack[-1]
        
    def pushStack(self, data):
        self.stack.append(data)
        
    def popStack(self):
        if len(self.stack) <= 0:
            print('Stack is empty')
        else:
            return self.stack.pop()
            
    def printStack(self):
        for i in self.stack:
            print(i)
            
stack = Stack()
stack.pushStack('First element')
stack.pushStack('Second element')
print(stack.peek())
stack.pushStack('Third element')
stack.pushStack('Fourth element')
print(stack.peek())
stack.printStack()
stack.popStack()
stack.printStack()