# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 14:36:15 2019

@author: HARSH
"""

import collections

deq = collections.deque(['Mon', 'Tue', 'Thu'])
deq.append('Fri')
deq.appendleft('Sun')
print(*deq)
deq.pop()
deq.popleft()
print(*deq)