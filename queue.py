# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 09:19:10 2019

@author: HARSH
"""

class Queue:
    def __init__(self):
        self.queue = []
        
    def insertQueue(self, data):
        self.queue.insert(0, data)
        
    def deleteQueue(self):
        if len(self.queue) <= 0:
            print('Queue is empty')
        else:
            return self.queue.pop()
            
    def size(self):
        return len(self.queue)
        
    def printQueue(self):
        for i in range(len(self.queue) - 1, -1, -1):
            print(self.queue[i])
            
queue = Queue()
queue.insertQueue('First value')
queue.insertQueue('Second value')
queue.insertQueue('Third value')
queue.printQueue()
print(queue.size())
queue.deleteQueue()
print(queue.size())
queue.printQueue()